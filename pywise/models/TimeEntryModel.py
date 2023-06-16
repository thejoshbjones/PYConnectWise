from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.TimeSheetReferenceModel import TimeSheetReferenceModel
from pywise.models.TicketReferenceModel import TicketReferenceModel
from pywise.models.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel
class ChargeToType(str, Enum):
    ServiceTicket = 'ServiceTicket'
    ProjectTicket = 'ProjectTicket'
    ChargeCode = 'ChargeCode'
    Activity = 'Activity'
class BillableOption(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class Status(str, Enum):
    Open = 'Open'
    Rejected = 'Rejected'
    PendingApproval = 'PendingApproval'
    ErrorsCorrected = 'ErrorsCorrected'
    PendingProjectApproval = 'PendingProjectApproval'
    ApprovedByTierOne = 'ApprovedByTierOne'
    RejectBySecondTier = 'RejectBySecondTier'
    ApprovedByTierTwo = 'ApprovedByTierTwo'
    ReadyToBill = 'ReadyToBill'
    Billed = 'Billed'
    WrittenOff = 'WrittenOff'
    BilledAgreement = 'BilledAgreement'

class TimeEntryModel(ConnectWiseModel):
    id: int | None
    company: CompanyReferenceModel | None
    charge_to_id: int | None
    charge_to_type: ChargeToType | None
    member: MemberReferenceModel | None
    location_id: int | None
    business_unit_id: int | None
    work_type: WorkTypeReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    agreement: AgreementReferenceModel | None
    time_start: str | None
    time_end: str | None
    hours_deduct: float | None
    actual_hours: float | None
    billable_option: BillableOption | None
    notes: str | None
    internal_notes: str | None
    add_to_detail_description_flag: bool | None
    add_to_internal_analysis_flag: bool | None
    add_to_resolution_flag: bool | None
    email_resource_flag: bool | None
    email_contact_flag: bool | None
    email_cc_flag: bool | None
    email_cc: str | None
    hours_billed: float | None
    invoice_hours: float | None
    entered_by: str | None
    date_entered: str | None
    invoice: InvoiceReferenceModel | None
    mobile_guid: str | None
    hourly_rate: float | None
    overage_rate: float | None
    agreement_hours: float | None
    agreement_amount: float | None
    time_sheet: TimeSheetReferenceModel | None
    status: Status | None
    ticket: TicketReferenceModel | None
    project: ProjectReferenceModel | None
    phase: ProjectPhaseReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True