from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.manage.ReminderReferenceModel import ReminderReferenceModel
from pywise.models.manage.ScheduleStatusReferenceModel import ScheduleStatusReferenceModel
from pywise.models.manage.ScheduleTypeReferenceModel import ScheduleTypeReferenceModel
from pywise.models.manage.ScheduleSpanReferenceModel import ScheduleSpanReferenceModel

class ScheduleEntryModel(ConnectWiseModel):
    id: int
    object_id: int
    name: str
    member: MemberReferenceModel
    where: ServiceLocationReferenceModel
    date_start: str
    date_end: str
    reminder: ReminderReferenceModel
    status: ScheduleStatusReferenceModel
    type: ScheduleTypeReferenceModel
    span: ScheduleSpanReferenceModel
    done_flag: bool
    acknowledged_flag: bool
    owner_flag: bool
    meeting_flag: bool
    allow_schedule_conflicts_flag: bool
    add_member_to_project_flag: bool
    project_role_id: int
    mobile_guid: str
    acknowledged_date: str
    close_date: str
    hours: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True