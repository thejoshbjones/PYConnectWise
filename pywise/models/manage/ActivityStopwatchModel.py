from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
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

class ActivityStopwatchModel(ConnectWiseModel):
    _info: dict[str, str]
    activity_id: int
    activity_mobile_guid: str
    agreement: AgreementReferenceModel
    billable_option: BillableOption
    business_unit_id: int
    date_entered: str
    end_time: str
    id: int
    internal_notes: str
    location_id: int
    member: MemberReferenceModel
    mobile_guid: str
    notes: str
    start_time: str
    status: Status
    total_pause_time: int
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True