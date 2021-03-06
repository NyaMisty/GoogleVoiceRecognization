# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='result.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cresult.proto\"{\n\x12\x46inalResultContent\x12\x0e\n\x06result\x18\x01 \x01(\x0c\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x17\n\x0ftokenizedResult\x18\x0c \x01(\x0c\x12\x0c\n\x04unk2\x18\x12 \x01(\x02\x12\x0c\n\x04unk3\x18\x13 \x01(\x02\x12\x0c\n\x04unk4\x18\x14 \x01(\x02\"O\n\x0b\x46inalResult\x12\x0c\n\x04unk1\x18\x01 \x01(\x05\x12\x0c\n\x04unk2\x18\x02 \x01(\x05\x12$\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x13.FinalResultContent\"4\n\x11PartialResultPart\x12\x0c\n\x04text\x18\x01 \x01(\x0c\x12\x11\n\tstability\x18\x02 \x01(\x02\"`\n\rPartialResult\x12%\n\tpartArray\x18\x01 \x03(\x0b\x32\x12.PartialResultPart\x12\x0c\n\x04unk1\x18\x02 \x01(\x05\x12\x0c\n\x04unk2\x18\x03 \x01(\x05\x12\x0c\n\x04unk3\x18\x10 \x01(\x05\"}\n\x10RecognitionEvent\x12\x11\n\teventType\x18\x01 \x01(\x05\x12\x0c\n\x04unk1\x18\x02 \x01(\x05\x12!\n\x0b\x66inalResult\x18\x03 \x01(\x0b\x32\x0c.FinalResult\x12%\n\rpartialResult\x18\x04 \x01(\x0b\x32\x0e.PartialResult\"g\n\x0fRecognizerEvent\x12,\n\x11recognititonEvent\x18\x01 \x01(\x0b\x32\x11.RecognitionEvent\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x14\n\x0clastLanguage\x18\x04 \x01(\t\"\\\n\x11RecognizeResponse\x12\x0b\n\x03seq\x18\x05 \x01(\x05\x12\r\n\x05isEnd\x18\x01 \x01(\x05\x12+\n\x0frecognizerEvent\x18\xf9\xc1L \x01(\x0b\x32\x10.RecognizerEventb\x06proto3'
)




_FINALRESULTCONTENT = _descriptor.Descriptor(
  name='FinalResultContent',
  full_name='FinalResultContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='FinalResultContent.result', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='FinalResultContent.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenizedResult', full_name='FinalResultContent.tokenizedResult', index=2,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk2', full_name='FinalResultContent.unk2', index=3,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk3', full_name='FinalResultContent.unk3', index=4,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk4', full_name='FinalResultContent.unk4', index=5,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=139,
)


_FINALRESULT = _descriptor.Descriptor(
  name='FinalResult',
  full_name='FinalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unk1', full_name='FinalResult.unk1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk2', full_name='FinalResult.unk2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='FinalResult.content', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=220,
)


_PARTIALRESULTPART = _descriptor.Descriptor(
  name='PartialResultPart',
  full_name='PartialResultPart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='PartialResultPart.text', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stability', full_name='PartialResultPart.stability', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=274,
)


_PARTIALRESULT = _descriptor.Descriptor(
  name='PartialResult',
  full_name='PartialResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partArray', full_name='PartialResult.partArray', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk1', full_name='PartialResult.unk1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk2', full_name='PartialResult.unk2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk3', full_name='PartialResult.unk3', index=3,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=372,
)


_RECOGNITIONEVENT = _descriptor.Descriptor(
  name='RecognitionEvent',
  full_name='RecognitionEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventType', full_name='RecognitionEvent.eventType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk1', full_name='RecognitionEvent.unk1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finalResult', full_name='RecognitionEvent.finalResult', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partialResult', full_name='RecognitionEvent.partialResult', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=499,
)


_RECOGNIZEREVENT = _descriptor.Descriptor(
  name='RecognizerEvent',
  full_name='RecognizerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recognititonEvent', full_name='RecognizerEvent.recognititonEvent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='RecognizerEvent.language', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastLanguage', full_name='RecognizerEvent.lastLanguage', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=604,
)


_RECOGNIZERESPONSE = _descriptor.Descriptor(
  name='RecognizeResponse',
  full_name='RecognizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='RecognizeResponse.seq', index=0,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isEnd', full_name='RecognizeResponse.isEnd', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recognizerEvent', full_name='RecognizeResponse.recognizerEvent', index=2,
      number=1253625, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=698,
)

_FINALRESULT.fields_by_name['content'].message_type = _FINALRESULTCONTENT
_PARTIALRESULT.fields_by_name['partArray'].message_type = _PARTIALRESULTPART
_RECOGNITIONEVENT.fields_by_name['finalResult'].message_type = _FINALRESULT
_RECOGNITIONEVENT.fields_by_name['partialResult'].message_type = _PARTIALRESULT
_RECOGNIZEREVENT.fields_by_name['recognititonEvent'].message_type = _RECOGNITIONEVENT
_RECOGNIZERESPONSE.fields_by_name['recognizerEvent'].message_type = _RECOGNIZEREVENT
DESCRIPTOR.message_types_by_name['FinalResultContent'] = _FINALRESULTCONTENT
DESCRIPTOR.message_types_by_name['FinalResult'] = _FINALRESULT
DESCRIPTOR.message_types_by_name['PartialResultPart'] = _PARTIALRESULTPART
DESCRIPTOR.message_types_by_name['PartialResult'] = _PARTIALRESULT
DESCRIPTOR.message_types_by_name['RecognitionEvent'] = _RECOGNITIONEVENT
DESCRIPTOR.message_types_by_name['RecognizerEvent'] = _RECOGNIZEREVENT
DESCRIPTOR.message_types_by_name['RecognizeResponse'] = _RECOGNIZERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FinalResultContent = _reflection.GeneratedProtocolMessageType('FinalResultContent', (_message.Message,), {
  'DESCRIPTOR' : _FINALRESULTCONTENT,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:FinalResultContent)
  })
_sym_db.RegisterMessage(FinalResultContent)

FinalResult = _reflection.GeneratedProtocolMessageType('FinalResult', (_message.Message,), {
  'DESCRIPTOR' : _FINALRESULT,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:FinalResult)
  })
_sym_db.RegisterMessage(FinalResult)

PartialResultPart = _reflection.GeneratedProtocolMessageType('PartialResultPart', (_message.Message,), {
  'DESCRIPTOR' : _PARTIALRESULTPART,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:PartialResultPart)
  })
_sym_db.RegisterMessage(PartialResultPart)

PartialResult = _reflection.GeneratedProtocolMessageType('PartialResult', (_message.Message,), {
  'DESCRIPTOR' : _PARTIALRESULT,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:PartialResult)
  })
_sym_db.RegisterMessage(PartialResult)

RecognitionEvent = _reflection.GeneratedProtocolMessageType('RecognitionEvent', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONEVENT,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:RecognitionEvent)
  })
_sym_db.RegisterMessage(RecognitionEvent)

RecognizerEvent = _reflection.GeneratedProtocolMessageType('RecognizerEvent', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZEREVENT,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:RecognizerEvent)
  })
_sym_db.RegisterMessage(RecognizerEvent)

RecognizeResponse = _reflection.GeneratedProtocolMessageType('RecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZERESPONSE,
  '__module__' : 'result_pb2'
  # @@protoc_insertion_point(class_scope:RecognizeResponse)
  })
_sym_db.RegisterMessage(RecognizeResponse)


# @@protoc_insertion_point(module_scope)
