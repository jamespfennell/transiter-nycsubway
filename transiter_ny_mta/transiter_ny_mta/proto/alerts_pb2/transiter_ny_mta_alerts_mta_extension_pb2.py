# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transiter-ny-mta-alerts-mta-extension.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import (
    transiter_ny_mta_alerts_gtfs_rt_base_pb2 as transiter__ny__mta__alerts__gtfs__rt__base__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="transiter-ny-mta-alerts-mta-extension.proto",
    package="transiter_ny_mta_alerts",
    syntax="proto2",
    serialized_options=_b('\n"com.github.transiter-ny-mta.alerts'),
    serialized_pb=_b(
        '\n+transiter-ny-mta-alerts-mta-extension.proto\x12\x17transiter_ny_mta_alerts\x1a*transiter-ny-mta-alerts-gtfs-rt-base.proto",\n\x11MercuryFeedHeader\x12\x17\n\x0fmercury_version\x18\x01 \x02(\t"J\n\x0cMercuryAlert\x12\x12\n\ncreated_at\x18\x01 \x02(\x04\x12\x12\n\nupdated_at\x18\x02 \x02(\x04\x12\x12\n\nalert_type\x18\x03 \x02(\t"\xd9\x08\n\x15MercuryEntitySelector\x12\x12\n\nsort_order\x18\x01 \x02(\t"\xdc\x04\n\x08Priority\x12!\n\x1dPRIORITY_NO_SCHEDULED_SERVICE\x10\x01\x12\x1c\n\x18PRIORITY_SUNDAY_SCHEDULE\x10\x02\x12\x1e\n\x1aPRIORITY_SATURDAY_SCHEDULE\x10\x03\x12\x1c\n\x18PRIORITY_HOLIDAY_SERVICE\x10\x04\x12\x1a\n\x16PRIORITY_EXTRA_SERVICE\x10\x05\x12\x19\n\x15PRIORITY_PLANNED_WORK\x10\x06\x12\x18\n\x14PRIORITY_ON_OR_CLOSE\x10\x07\x12\x18\n\x14PRIORITY_SLOW_SPEEDS\x10\x08\x12\x18\n\x14PRIORITY_SOME_DELAYS\x10\t\x12\x1a\n\x16PRIORITY_SPECIAL_EVENT\x10\n\x12\x1d\n\x19PRIORITY_STATIONS_SKIPPED\x10\x0b\x12\x13\n\x0fPRIORITY_DELAYS\x10\x0c\x12\x1d\n\x19PRIORITY_EXPRESS_TO_LOCAL\x10\r\x12\x1a\n\x16PRIORITY_SOME_REROUTES\x10\x0e\x12\x1d\n\x19PRIORITY_LOCAL_TO_EXPRESS\x10\x0f\x12\x1b\n\x17PRIORITY_SERVICE_CHANGE\x10\x10\x12\x1c\n\x18PRIORITY_TRAINS_REROUTED\x10\x11\x12\x1b\n\x17PRIORITY_PART_SUSPENDED\x10\x12\x12\x1d\n\x19PRIORITY_MULTIPLE_IMPACTS\x10\x13\x12\x16\n\x12PRIORITY_SUSPENDED\x10\x14\x12\x13\n\x0fPRIORITY_BUSING\x10\x15"\xcc\x03\n\x0fNyctBusPriority\x12*\n&NYCT_BUS_PRIORITY_NO_SCHEDULED_SERVICE\x10\x01\x12%\n!NYCT_BUS_PRIORITY_SUNDAY_SCHEDULE\x10\x02\x12\'\n#NYCT_BUS_PRIORITY_SATURDAY_SCHEDULE\x10\x03\x12%\n!NYCT_BUS_PRIORITY_HOLIDAY_SERVICE\x10\x04\x12$\n NYCT_BUS_PRIORITY_PLANNED_DETOUR\x10\x05\x12#\n\x1fNYCT_BUS_PRIORITY_EXTRA_SERVICE\x10\x06\x12"\n\x1eNYCT_BUS_PRIORITY_PLANNED_WORK\x10\x07\x12#\n\x1fNYCT_BUS_PRIORITY_SPECIAL_EVENT\x10\x0b\x12\x1c\n\x18NYCT_BUS_PRIORITY_DELAYS\x10\r\x12\x1d\n\x19NYCT_BUS_PRIORITY_DETOURS\x10\x10\x12$\n NYCT_BUS_PRIORITY_SERVICE_CHANGE\x10\x12\x12\x1f\n\x1bNYCT_BUS_PRIORITY_SUSPENDED\x10\x16:m\n\x13mercury_feed_header\x12#.transiter_ny_mta_alerts.FeedHeader\x18\xe9\x07 \x01(\x0b\x32*.transiter_ny_mta_alerts.MercuryFeedHeader:]\n\rmercury_alert\x12\x1e.transiter_ny_mta_alerts.Alert\x18\xe9\x07 \x01(\x0b\x32%.transiter_ny_mta_alerts.MercuryAlert:y\n\x17mercury_entity_selector\x12\'.transiter_ny_mta_alerts.EntitySelector\x18\xe9\x07 \x01(\x0b\x32..transiter_ny_mta_alerts.MercuryEntitySelectorB$\n"com.github.transiter-ny-mta.alerts'
    ),
    dependencies=[transiter__ny__mta__alerts__gtfs__rt__base__pb2.DESCRIPTOR,],
)


MERCURY_FEED_HEADER_FIELD_NUMBER = 1001
mercury_feed_header = _descriptor.FieldDescriptor(
    name="mercury_feed_header",
    full_name="transiter_ny_mta_alerts.mercury_feed_header",
    index=0,
    number=1001,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
)
MERCURY_ALERT_FIELD_NUMBER = 1001
mercury_alert = _descriptor.FieldDescriptor(
    name="mercury_alert",
    full_name="transiter_ny_mta_alerts.mercury_alert",
    index=1,
    number=1001,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
)
MERCURY_ENTITY_SELECTOR_FIELD_NUMBER = 1001
mercury_entity_selector = _descriptor.FieldDescriptor(
    name="mercury_entity_selector",
    full_name="transiter_ny_mta_alerts.mercury_entity_selector",
    index=2,
    number=1001,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
)

_MERCURYENTITYSELECTOR_PRIORITY = _descriptor.EnumDescriptor(
    name="Priority",
    full_name="transiter_ny_mta_alerts.MercuryEntitySelector.Priority",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_NO_SCHEDULED_SERVICE",
            index=0,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SUNDAY_SCHEDULE",
            index=1,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SATURDAY_SCHEDULE",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_HOLIDAY_SERVICE",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_EXTRA_SERVICE",
            index=4,
            number=5,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PLANNED_WORK",
            index=5,
            number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_ON_OR_CLOSE",
            index=6,
            number=7,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SLOW_SPEEDS",
            index=7,
            number=8,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SOME_DELAYS",
            index=8,
            number=9,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SPECIAL_EVENT",
            index=9,
            number=10,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_STATIONS_SKIPPED",
            index=10,
            number=11,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_DELAYS",
            index=11,
            number=12,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_EXPRESS_TO_LOCAL",
            index=12,
            number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SOME_REROUTES",
            index=13,
            number=14,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_LOCAL_TO_EXPRESS",
            index=14,
            number=15,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SERVICE_CHANGE",
            index=15,
            number=16,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_TRAINS_REROUTED",
            index=16,
            number=17,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_PART_SUSPENDED",
            index=17,
            number=18,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_MULTIPLE_IMPACTS",
            index=18,
            number=19,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_SUSPENDED",
            index=19,
            number=20,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIORITY_BUSING",
            index=20,
            number=21,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=285,
    serialized_end=889,
)
_sym_db.RegisterEnumDescriptor(_MERCURYENTITYSELECTOR_PRIORITY)

_MERCURYENTITYSELECTOR_NYCTBUSPRIORITY = _descriptor.EnumDescriptor(
    name="NyctBusPriority",
    full_name="transiter_ny_mta_alerts.MercuryEntitySelector.NyctBusPriority",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_NO_SCHEDULED_SERVICE",
            index=0,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_SUNDAY_SCHEDULE",
            index=1,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_SATURDAY_SCHEDULE",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_HOLIDAY_SERVICE",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_PLANNED_DETOUR",
            index=4,
            number=5,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_EXTRA_SERVICE",
            index=5,
            number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_PLANNED_WORK",
            index=6,
            number=7,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_SPECIAL_EVENT",
            index=7,
            number=11,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_DELAYS",
            index=8,
            number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_DETOURS",
            index=9,
            number=16,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_SERVICE_CHANGE",
            index=10,
            number=18,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NYCT_BUS_PRIORITY_SUSPENDED",
            index=11,
            number=22,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=892,
    serialized_end=1352,
)
_sym_db.RegisterEnumDescriptor(_MERCURYENTITYSELECTOR_NYCTBUSPRIORITY)


_MERCURYFEEDHEADER = _descriptor.Descriptor(
    name="MercuryFeedHeader",
    full_name="transiter_ny_mta_alerts.MercuryFeedHeader",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="mercury_version",
            full_name="transiter_ny_mta_alerts.MercuryFeedHeader.mercury_version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=116,
    serialized_end=160,
)


_MERCURYALERT = _descriptor.Descriptor(
    name="MercuryAlert",
    full_name="transiter_ny_mta_alerts.MercuryAlert",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="created_at",
            full_name="transiter_ny_mta_alerts.MercuryAlert.created_at",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="updated_at",
            full_name="transiter_ny_mta_alerts.MercuryAlert.updated_at",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="alert_type",
            full_name="transiter_ny_mta_alerts.MercuryAlert.alert_type",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=162,
    serialized_end=236,
)


_MERCURYENTITYSELECTOR = _descriptor.Descriptor(
    name="MercuryEntitySelector",
    full_name="transiter_ny_mta_alerts.MercuryEntitySelector",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="sort_order",
            full_name="transiter_ny_mta_alerts.MercuryEntitySelector.sort_order",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _MERCURYENTITYSELECTOR_PRIORITY,
        _MERCURYENTITYSELECTOR_NYCTBUSPRIORITY,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=239,
    serialized_end=1352,
)

_MERCURYENTITYSELECTOR_PRIORITY.containing_type = _MERCURYENTITYSELECTOR
_MERCURYENTITYSELECTOR_NYCTBUSPRIORITY.containing_type = _MERCURYENTITYSELECTOR
DESCRIPTOR.message_types_by_name["MercuryFeedHeader"] = _MERCURYFEEDHEADER
DESCRIPTOR.message_types_by_name["MercuryAlert"] = _MERCURYALERT
DESCRIPTOR.message_types_by_name["MercuryEntitySelector"] = _MERCURYENTITYSELECTOR
DESCRIPTOR.extensions_by_name["mercury_feed_header"] = mercury_feed_header
DESCRIPTOR.extensions_by_name["mercury_alert"] = mercury_alert
DESCRIPTOR.extensions_by_name["mercury_entity_selector"] = mercury_entity_selector
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MercuryFeedHeader = _reflection.GeneratedProtocolMessageType(
    "MercuryFeedHeader",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MERCURYFEEDHEADER,
        __module__="transiter_ny_mta_alerts_mta_extension_pb2"
        # @@protoc_insertion_point(class_scope:transiter_ny_mta_alerts.MercuryFeedHeader)
    ),
)
_sym_db.RegisterMessage(MercuryFeedHeader)

MercuryAlert = _reflection.GeneratedProtocolMessageType(
    "MercuryAlert",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MERCURYALERT,
        __module__="transiter_ny_mta_alerts_mta_extension_pb2"
        # @@protoc_insertion_point(class_scope:transiter_ny_mta_alerts.MercuryAlert)
    ),
)
_sym_db.RegisterMessage(MercuryAlert)

MercuryEntitySelector = _reflection.GeneratedProtocolMessageType(
    "MercuryEntitySelector",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MERCURYENTITYSELECTOR,
        __module__="transiter_ny_mta_alerts_mta_extension_pb2"
        # @@protoc_insertion_point(class_scope:transiter_ny_mta_alerts.MercuryEntitySelector)
    ),
)
_sym_db.RegisterMessage(MercuryEntitySelector)

mercury_feed_header.message_type = _MERCURYFEEDHEADER
transiter__ny__mta__alerts__gtfs__rt__base__pb2.FeedHeader.RegisterExtension(
    mercury_feed_header
)
mercury_alert.message_type = _MERCURYALERT
transiter__ny__mta__alerts__gtfs__rt__base__pb2.Alert.RegisterExtension(mercury_alert)
mercury_entity_selector.message_type = _MERCURYENTITYSELECTOR
transiter__ny__mta__alerts__gtfs__rt__base__pb2.EntitySelector.RegisterExtension(
    mercury_entity_selector
)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
