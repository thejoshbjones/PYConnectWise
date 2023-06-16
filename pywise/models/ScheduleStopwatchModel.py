from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
class BillableOption(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class Status(str, Enum):
    Reset = 'Reset'
    Running = 'Running'
    Paused = 'Paused'
    Stopped = 'Stopped'

class ScheduleStopwatchModel(ConnectWiseModel):
    _info: dict[str, str] | None
    agreement: AgreementReferenceModel | None
    billable_option: BillableOption | None
    business_unit_id: int | None
    date_entered: str | None
    end_time: str | None
    id: int | None
    internal_notes: str | None
    location_id: int | None
    member: MemberReferenceModel | None
    mobile_guid: str | None
    notes: str | None
    schedule_id: int | None
    schedule_mobile_guid: str | None
    start_time: str | None
    status: Status | None
    total_pause_time: int | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True