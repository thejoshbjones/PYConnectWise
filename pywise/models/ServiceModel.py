from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.CalendarSetupReferenceModel import CalendarSetupReferenceModel
class SrNotify(str, Enum):
    All = 'All'
    NewAndClosedRequests = 'NewAndClosedRequests'
    ClosedRequestsOnly = 'ClosedRequestsOnly'
    NewRequestsOnly = 'NewRequestsOnly'
    NONE = 'NONE'
class ScheduleSpan(str, Enum):
    Standard = 'Standard'
    OfficeHours = 'OfficeHours'
    Overnight = 'Overnight'

class ServiceModel(ConnectWiseModel):
    id: int | None
    sr_notify: SrNotify | None
    schedule_span: ScheduleSpan | None
    hide_delimiter_flag: bool | None
    allow_c_c_flag: bool | None
    allow_t_o_flag: bool | None
    header_color: str | None
    member_color: str | None
    contact_color: str | None
    unknown_color: str | None
    calendar_setup: CalendarSetupReferenceModel | None
    header_color_disable_flag: bool | None
    member_color_disable_flag: bool | None
    contact_color_disable_flag: bool | None
    unknown_color_disable_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True