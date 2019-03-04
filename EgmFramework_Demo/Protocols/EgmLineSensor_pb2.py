# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='EgmLineSensor.proto',
  package='lth.egm',
  serialized_pb='\n\x13\x45gmLineSensor.proto\x12\x07lth.egm\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\"\xa3\x01\n\nLineSensor\x12#\n\x0bsensedPoint\x18\x01 \x02(\x0b\x32\x0e.lth.egm.Point\x12\x1d\n\x05start\x18\x02 \x02(\x0b\x32\x0e.lth.egm.Point\x12\x1b\n\x03\x65nd\x18\x03 \x02(\x0b\x32\x0e.lth.egm.Point\x12\x0e\n\x06radius\x18\x04 \x02(\x01\x12\x12\n\nsensedPart\x18\x05 \x02(\t\x12\x10\n\x08sensorID\x18\x06 \x02(\r')




_POINT = descriptor.Descriptor(
  name='Point',
  full_name='lth.egm.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='lth.egm.Point.x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='lth.egm.Point.y', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='lth.egm.Point.z', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=32,
  serialized_end=72,
)


_LINESENSOR = descriptor.Descriptor(
  name='LineSensor',
  full_name='lth.egm.LineSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sensedPoint', full_name='lth.egm.LineSensor.sensedPoint', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start', full_name='lth.egm.LineSensor.start', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end', full_name='lth.egm.LineSensor.end', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='radius', full_name='lth.egm.LineSensor.radius', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sensedPart', full_name='lth.egm.LineSensor.sensedPart', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sensorID', full_name='lth.egm.LineSensor.sensorID', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=75,
  serialized_end=238,
)

_LINESENSOR.fields_by_name['sensedPoint'].message_type = _POINT
_LINESENSOR.fields_by_name['start'].message_type = _POINT
_LINESENSOR.fields_by_name['end'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['LineSensor'] = _LINESENSOR

class Point(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POINT
  
  # @@protoc_insertion_point(class_scope:lth.egm.Point)

class LineSensor(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LINESENSOR
  
  # @@protoc_insertion_point(class_scope:lth.egm.LineSensor)

# @@protoc_insertion_point(module_scope)