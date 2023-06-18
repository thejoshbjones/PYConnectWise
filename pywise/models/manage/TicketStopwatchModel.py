from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
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

class TicketStopwatchModel(ConnectWiseModel):
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
    service_status: ServiceStatusReferenceModel | None
    start_time: str | None
    status: Status | None
    ticket: TicketReferenceModel | None
    ticket_mobile_guid: str | None
    total_pause_time: int | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    show_notes_in_discussion_flag: bool | None
    show_notes_in_internal_flag: bool | None
    show_notes_in_resolution_flag: bool | None
    email_notes_to_contact_flag: bool | None
    email_notes_to_resources_flag: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True