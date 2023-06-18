from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.ReminderReferenceModel import ReminderReferenceModel
from pywise.models.ScheduleStatusReferenceModel import ScheduleStatusReferenceModel
from pywise.models.ScheduleTypeReferenceModel import ScheduleTypeReferenceModel
from pywise.models.ScheduleSpanReferenceModel import ScheduleSpanReferenceModel

class ScheduleEntryModel(ConnectWiseModel):
    id: int | None
    object_id: int | None
    name: str | None
    member: MemberReferenceModel | None
    where: ServiceLocationReferenceModel | None
    date_start: str | None
    date_end: str | None
    reminder: ReminderReferenceModel | None
    status: ScheduleStatusReferenceModel | None
    type: ScheduleTypeReferenceModel | None
    span: ScheduleSpanReferenceModel | None
    done_flag: bool | None
    acknowledged_flag: bool | None
    owner_flag: bool | None
    meeting_flag: bool | None
    allow_schedule_conflicts_flag: bool | None
    add_member_to_project_flag: bool | None
    project_role_id: int | None
    mobile_guid: str | None
    acknowledged_date: str | None
    close_date: str | None
    hours: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True