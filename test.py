#/usr/bin/python2
import sys
import socket
import ssl
import struct
import time
import threading
from speex import *
from speech_pb2 import *
from result_pb2 import *

context = ssl.create_default_context()
hostname = 'vs.google.com'
rsock = socket.create_connection((hostname, 14259))
sock = context.wrap_socket(rsock, server_hostname=hostname)

# initial header, fixed
sock.send(b"0000c548232af5c805ff".decode('hex'))

# all following packet format: 4byte length + protobuf data
def sendReq(data):
    return sock.send(struct.pack(">I", len(data)) + data)

# contains the client info, change it if needed
initialReq = SpeechInitialRequest()
initialReq.ParseFromString(b"0A0A7265636F676E697A6572C2888F0142120F0A0B636D6E2D68616E732D636E10011A090A057A682D434E10012A2434333231353633342D453535342D343344442D414246332D364232374543433331373136E28E8F01071500007A46180682C78F014D12097472616E736C6174654203694F534A0431332E355209362E382E35393137375A0A6950686F6E6531302C3260E005689E0370A301820114636F6D2E676F6F676C652E5472616E736C617465A2E68F01530A380A14636F6D2E676F6F676C652E5472616E736C6174655A097472616E736C6174659A0114636F6D2E676F6F676C652E5472616E736C61746518012801380045000000005800600068007000A00101B0010192D180F801071500007A4618068AC6D1A702020800".decode('hex'))
initialReq.userInfo.spokenLanguage.locale = sys.argv[2] #"ja-JP" # change the recognition language here, the default is chinese recognization (cmn-hans-cn)
print "Use initial request: ", initialReq
sendReq(initialReq.SerializeToString())


# the response packet arrives progressively, so we receive them in a thread
def recvn(n):
    ret = b''
    while True:
        c = sock.recv(n)
        if not c:
            break
        ret += c
        n -= len(c)
    return ret

class RecvTh(threading.Thread):
    def run(self):
        while True:
            lbuf = recvn(4)
            l = struct.unpack(">I", lbuf)[0]
            proto = recvn(l)
            resp = RecognizeResponse()
            resp.ParseFromString(proto)
            print resp
            if resp.isEnd:
                break
th = RecvTh()
th.start()

pcm = open(sys.argv[1], 'rb').read() # 16bit, 16000Hz RAW PCM Data

def sendAudio(audio):
    req = AudioRequest()
    req.audioData.audioData = audio
    return sendReq(req.SerializeToString())


encoder = WBEncoder()
packet_size = encoder.frame_size * 2 * 1
print('frame size: %d' % encoder.frame_size)

def psize(size):
    buffer = b''
    mask = 0
    while (size > 0):
        buffer = chr((size % 2**7) | mask) + buffer
        mask = 0x80
        size >>= 7
    return buffer

# maybe we need some empty padding, but the testing shows that we needn't
#sendAudio(encoder.encode('\x00' * packet_size)) # padding
#sendAudio(encoder.encode('\x00' * packet_size) * 3) # padding

vocoded = b''

for cur, i in enumerate(range(0, len(pcm), packet_size)):
    if (cur + 1) % 10 == 0: # google sends 10 frames each request, I tried to send them in one request, but it seems this will lower the accuracy 
        sendAudio(vocoded)
        vocoded = b''
    packet = pcm[i:i + packet_size]
    if len(packet) != packet_size:
        packet += b'\x00' * (packet_size - len(packet) % packet_size) # padding if the last pcm segment does not fit
        
    raw = encoder.encode(packet)
    vocoded += psize(len(raw)) + raw
    time.sleep(0.005)

sendAudio(vocoded)

"""
spx = open('test.spx', 'rb').read()
# test stub
for cur, i in enumerate(range(0, len(spx), 71)):
    if (cur - 1) % 10 == 0:
        sendAudio(vocoded)
        vocoded = b''
    vocoded += spx[i:i+71]

sendAudio(vocoded)
"""

# ending
sendReq('\x18\x01')

th.join()