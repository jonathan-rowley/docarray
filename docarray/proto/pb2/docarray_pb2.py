# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: docarray.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x64ocarray.proto\x12\x08\x64ocarray\x1a\x1cgoogle/protobuf/struct.proto\"A\n\x11\x44\x65nseNdArrayProto\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\r\n\x05shape\x18\x02 \x03(\r\x12\r\n\x05\x64type\x18\x03 \x01(\t\"g\n\x0cNdArrayProto\x12*\n\x05\x64\x65nse\x18\x01 \x01(\x0b\x32\x1b.docarray.DenseNdArrayProto\x12+\n\nparameters\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"Z\n\x0cKeyValuePair\x12#\n\x03key\x18\x01 \x01(\x0b\x32\x16.google.protobuf.Value\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\";\n\x10GenericDictValue\x12\'\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x16.docarray.KeyValuePair\"\xb1\x03\n\tNodeProto\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x11\n\x07integer\x18\x02 \x01(\x05H\x00\x12\x0f\n\x05\x66loat\x18\x03 \x01(\x01H\x00\x12\x11\n\x07\x62oolean\x18\x04 \x01(\x08H\x00\x12\x0e\n\x04\x62lob\x18\x05 \x01(\x0cH\x00\x12)\n\x07ndarray\x18\x06 \x01(\x0b\x32\x16.docarray.NdArrayProtoH\x00\x12!\n\x03\x64oc\x18\x07 \x01(\x0b\x32\x12.docarray.DocProtoH\x00\x12+\n\tdoc_array\x18\x08 \x01(\x0b\x32\x16.docarray.DocListProtoH\x00\x12(\n\x04list\x18\t \x01(\x0b\x32\x18.docarray.ListOfAnyProtoH\x00\x12\'\n\x03set\x18\n \x01(\x0b\x32\x18.docarray.ListOfAnyProtoH\x00\x12)\n\x05tuple\x18\x0b \x01(\x0b\x32\x18.docarray.ListOfAnyProtoH\x00\x12(\n\x04\x64ict\x18\x0c \x01(\x0b\x32\x18.docarray.DictOfAnyProtoH\x00\x12\x0e\n\x04type\x18\r \x01(\tH\x01\x42\t\n\x07\x63ontentB\x0f\n\rdocarray_type\"x\n\x08\x44ocProto\x12*\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1c.docarray.DocProto.DataEntry\x1a@\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.docarray.NodeProto:\x02\x38\x01\"\x84\x01\n\x0e\x44ictOfAnyProto\x12\x30\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\".docarray.DictOfAnyProto.DataEntry\x1a@\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.docarray.NodeProto:\x02\x38\x01\"3\n\x0eListOfAnyProto\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.docarray.NodeProto\"0\n\x0c\x44ocListProto\x12 \n\x04\x64ocs\x18\x01 \x03(\x0b\x32\x12.docarray.DocProto\";\n\x13ListOfDocArrayProto\x12$\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x16.docarray.DocListProto\"8\n\x11ListOfDocVecProto\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.docarray.DocVecProto\"\xc5\x04\n\x0b\x44ocVecProto\x12@\n\x0etensor_columns\x18\x01 \x03(\x0b\x32(.docarray.DocVecProto.TensorColumnsEntry\x12:\n\x0b\x64oc_columns\x18\x02 \x03(\x0b\x32%.docarray.DocVecProto.DocColumnsEntry\x12\x43\n\x10\x64ocs_vec_columns\x18\x03 \x03(\x0b\x32).docarray.DocVecProto.DocsVecColumnsEntry\x12:\n\x0b\x61ny_columns\x18\x04 \x03(\x0b\x32%.docarray.DocVecProto.AnyColumnsEntry\x1aL\n\x12TensorColumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.docarray.NdArrayProto:\x02\x38\x01\x1aH\n\x0f\x44ocColumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.docarray.DocVecProto:\x02\x38\x01\x1aR\n\x13\x44ocsVecColumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.docarray.ListOfDocVecProto:\x02\x38\x01\x1aK\n\x0f\x41nyColumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.docarray.ListOfAnyProto:\x02\x38\x01\x62\x06proto3'
)


_DENSENDARRAYPROTO = DESCRIPTOR.message_types_by_name['DenseNdArrayProto']
_NDARRAYPROTO = DESCRIPTOR.message_types_by_name['NdArrayProto']
_KEYVALUEPAIR = DESCRIPTOR.message_types_by_name['KeyValuePair']
_GENERICDICTVALUE = DESCRIPTOR.message_types_by_name['GenericDictValue']
_NODEPROTO = DESCRIPTOR.message_types_by_name['NodeProto']
_DOCPROTO = DESCRIPTOR.message_types_by_name['DocProto']
_DOCPROTO_DATAENTRY = _DOCPROTO.nested_types_by_name['DataEntry']
_DICTOFANYPROTO = DESCRIPTOR.message_types_by_name['DictOfAnyProto']
_DICTOFANYPROTO_DATAENTRY = _DICTOFANYPROTO.nested_types_by_name['DataEntry']
_LISTOFANYPROTO = DESCRIPTOR.message_types_by_name['ListOfAnyProto']
_DOCLISTPROTO = DESCRIPTOR.message_types_by_name['DocListProto']
_LISTOFDOCARRAYPROTO = DESCRIPTOR.message_types_by_name['ListOfDocArrayProto']
_LISTOFDOCVECPROTO = DESCRIPTOR.message_types_by_name['ListOfDocVecProto']
_DOCVECPROTO = DESCRIPTOR.message_types_by_name['DocVecProto']
_DOCVECPROTO_TENSORCOLUMNSENTRY = _DOCVECPROTO.nested_types_by_name[
    'TensorColumnsEntry'
]
_DOCVECPROTO_DOCCOLUMNSENTRY = _DOCVECPROTO.nested_types_by_name['DocColumnsEntry']
_DOCVECPROTO_DOCSVECCOLUMNSENTRY = _DOCVECPROTO.nested_types_by_name[
    'DocsVecColumnsEntry'
]
_DOCVECPROTO_ANYCOLUMNSENTRY = _DOCVECPROTO.nested_types_by_name['AnyColumnsEntry']
DenseNdArrayProto = _reflection.GeneratedProtocolMessageType(
    'DenseNdArrayProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _DENSENDARRAYPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.DenseNdArrayProto)
    },
)
_sym_db.RegisterMessage(DenseNdArrayProto)

NdArrayProto = _reflection.GeneratedProtocolMessageType(
    'NdArrayProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _NDARRAYPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.NdArrayProto)
    },
)
_sym_db.RegisterMessage(NdArrayProto)

KeyValuePair = _reflection.GeneratedProtocolMessageType(
    'KeyValuePair',
    (_message.Message,),
    {
        'DESCRIPTOR': _KEYVALUEPAIR,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.KeyValuePair)
    },
)
_sym_db.RegisterMessage(KeyValuePair)

GenericDictValue = _reflection.GeneratedProtocolMessageType(
    'GenericDictValue',
    (_message.Message,),
    {
        'DESCRIPTOR': _GENERICDICTVALUE,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.GenericDictValue)
    },
)
_sym_db.RegisterMessage(GenericDictValue)

NodeProto = _reflection.GeneratedProtocolMessageType(
    'NodeProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _NODEPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.NodeProto)
    },
)
_sym_db.RegisterMessage(NodeProto)

DocProto = _reflection.GeneratedProtocolMessageType(
    'DocProto',
    (_message.Message,),
    {
        'DataEntry': _reflection.GeneratedProtocolMessageType(
            'DataEntry',
            (_message.Message,),
            {
                'DESCRIPTOR': _DOCPROTO_DATAENTRY,
                '__module__': 'docarray_pb2'
                # @@protoc_insertion_point(class_scope:docarray.DocProto.DataEntry)
            },
        ),
        'DESCRIPTOR': _DOCPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.DocProto)
    },
)
_sym_db.RegisterMessage(DocProto)
_sym_db.RegisterMessage(DocProto.DataEntry)

DictOfAnyProto = _reflection.GeneratedProtocolMessageType(
    'DictOfAnyProto',
    (_message.Message,),
    {
        'DataEntry': _reflection.GeneratedProtocolMessageType(
            'DataEntry',
            (_message.Message,),
            {
                'DESCRIPTOR': _DICTOFANYPROTO_DATAENTRY,
                '__module__': 'docarray_pb2'
                # @@protoc_insertion_point(class_scope:docarray.DictOfAnyProto.DataEntry)
            },
        ),
        'DESCRIPTOR': _DICTOFANYPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.DictOfAnyProto)
    },
)
_sym_db.RegisterMessage(DictOfAnyProto)
_sym_db.RegisterMessage(DictOfAnyProto.DataEntry)

ListOfAnyProto = _reflection.GeneratedProtocolMessageType(
    'ListOfAnyProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _LISTOFANYPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.ListOfAnyProto)
    },
)
_sym_db.RegisterMessage(ListOfAnyProto)

DocListProto = _reflection.GeneratedProtocolMessageType(
    'DocListProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _DOCLISTPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.DocListProto)
    },
)
_sym_db.RegisterMessage(DocListProto)

ListOfDocArrayProto = _reflection.GeneratedProtocolMessageType(
    'ListOfDocArrayProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _LISTOFDOCARRAYPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.ListOfDocArrayProto)
    },
)
_sym_db.RegisterMessage(ListOfDocArrayProto)

ListOfDocVecProto = _reflection.GeneratedProtocolMessageType(
    'ListOfDocVecProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _LISTOFDOCVECPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.ListOfDocVecProto)
    },
)
_sym_db.RegisterMessage(ListOfDocVecProto)

DocVecProto = _reflection.GeneratedProtocolMessageType(
    'DocVecProto',
    (_message.Message,),
    {
        'TensorColumnsEntry': _reflection.GeneratedProtocolMessageType(
            'TensorColumnsEntry',
            (_message.Message,),
            {
                'DESCRIPTOR': _DOCVECPROTO_TENSORCOLUMNSENTRY,
                '__module__': 'docarray_pb2'
                # @@protoc_insertion_point(class_scope:docarray.DocVecProto.TensorColumnsEntry)
            },
        ),
        'DocColumnsEntry': _reflection.GeneratedProtocolMessageType(
            'DocColumnsEntry',
            (_message.Message,),
            {
                'DESCRIPTOR': _DOCVECPROTO_DOCCOLUMNSENTRY,
                '__module__': 'docarray_pb2'
                # @@protoc_insertion_point(class_scope:docarray.DocVecProto.DocColumnsEntry)
            },
        ),
        'DocsVecColumnsEntry': _reflection.GeneratedProtocolMessageType(
            'DocsVecColumnsEntry',
            (_message.Message,),
            {
                'DESCRIPTOR': _DOCVECPROTO_DOCSVECCOLUMNSENTRY,
                '__module__': 'docarray_pb2'
                # @@protoc_insertion_point(class_scope:docarray.DocVecProto.DocsVecColumnsEntry)
            },
        ),
        'AnyColumnsEntry': _reflection.GeneratedProtocolMessageType(
            'AnyColumnsEntry',
            (_message.Message,),
            {
                'DESCRIPTOR': _DOCVECPROTO_ANYCOLUMNSENTRY,
                '__module__': 'docarray_pb2'
                # @@protoc_insertion_point(class_scope:docarray.DocVecProto.AnyColumnsEntry)
            },
        ),
        'DESCRIPTOR': _DOCVECPROTO,
        '__module__': 'docarray_pb2'
        # @@protoc_insertion_point(class_scope:docarray.DocVecProto)
    },
)
_sym_db.RegisterMessage(DocVecProto)
_sym_db.RegisterMessage(DocVecProto.TensorColumnsEntry)
_sym_db.RegisterMessage(DocVecProto.DocColumnsEntry)
_sym_db.RegisterMessage(DocVecProto.DocsVecColumnsEntry)
_sym_db.RegisterMessage(DocVecProto.AnyColumnsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _DOCPROTO_DATAENTRY._options = None
    _DOCPROTO_DATAENTRY._serialized_options = b'8\001'
    _DICTOFANYPROTO_DATAENTRY._options = None
    _DICTOFANYPROTO_DATAENTRY._serialized_options = b'8\001'
    _DOCVECPROTO_TENSORCOLUMNSENTRY._options = None
    _DOCVECPROTO_TENSORCOLUMNSENTRY._serialized_options = b'8\001'
    _DOCVECPROTO_DOCCOLUMNSENTRY._options = None
    _DOCVECPROTO_DOCCOLUMNSENTRY._serialized_options = b'8\001'
    _DOCVECPROTO_DOCSVECCOLUMNSENTRY._options = None
    _DOCVECPROTO_DOCSVECCOLUMNSENTRY._serialized_options = b'8\001'
    _DOCVECPROTO_ANYCOLUMNSENTRY._options = None
    _DOCVECPROTO_ANYCOLUMNSENTRY._serialized_options = b'8\001'
    _DENSENDARRAYPROTO._serialized_start = 58
    _DENSENDARRAYPROTO._serialized_end = 123
    _NDARRAYPROTO._serialized_start = 125
    _NDARRAYPROTO._serialized_end = 228
    _KEYVALUEPAIR._serialized_start = 230
    _KEYVALUEPAIR._serialized_end = 320
    _GENERICDICTVALUE._serialized_start = 322
    _GENERICDICTVALUE._serialized_end = 381
    _NODEPROTO._serialized_start = 384
    _NODEPROTO._serialized_end = 817
    _DOCPROTO._serialized_start = 819
    _DOCPROTO._serialized_end = 939
    _DOCPROTO_DATAENTRY._serialized_start = 875
    _DOCPROTO_DATAENTRY._serialized_end = 939
    _DICTOFANYPROTO._serialized_start = 942
    _DICTOFANYPROTO._serialized_end = 1074
    _DICTOFANYPROTO_DATAENTRY._serialized_start = 875
    _DICTOFANYPROTO_DATAENTRY._serialized_end = 939
    _LISTOFANYPROTO._serialized_start = 1076
    _LISTOFANYPROTO._serialized_end = 1127
    _DOCLISTPROTO._serialized_start = 1129
    _DOCLISTPROTO._serialized_end = 1177
    _LISTOFDOCARRAYPROTO._serialized_start = 1179
    _LISTOFDOCARRAYPROTO._serialized_end = 1238
    _LISTOFDOCVECPROTO._serialized_start = 1240
    _LISTOFDOCVECPROTO._serialized_end = 1296
    _DOCVECPROTO._serialized_start = 1299
    _DOCVECPROTO._serialized_end = 1880
    _DOCVECPROTO_TENSORCOLUMNSENTRY._serialized_start = 1569
    _DOCVECPROTO_TENSORCOLUMNSENTRY._serialized_end = 1645
    _DOCVECPROTO_DOCCOLUMNSENTRY._serialized_start = 1647
    _DOCVECPROTO_DOCCOLUMNSENTRY._serialized_end = 1719
    _DOCVECPROTO_DOCSVECCOLUMNSENTRY._serialized_start = 1721
    _DOCVECPROTO_DOCSVECCOLUMNSENTRY._serialized_end = 1803
    _DOCVECPROTO_ANYCOLUMNSENTRY._serialized_start = 1805
    _DOCVECPROTO_ANYCOLUMNSENTRY._serialized_end = 1880
# @@protoc_insertion_point(module_scope)
