from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ExpenseReportReferenceModel import ExpenseReportReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from enum import Enum
from pywise.models.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.PaymentMethodReferenceModel import PaymentMethodReferenceModel
from pywise.models.ClassificationReferenceModel import ClassificationReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.ExpenseTaxModel import ExpenseTaxModel
from pywise.models.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
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

class ExpenseEntryModel(ConnectWiseModel):
    id: int | None
    expense_report: ExpenseReportReferenceModel | None
    company: CompanyReferenceModel | None
    charge_to_id: int | None
    charge_to_type: ChargeToType | None
    type: ExpenseTypeReferenceModel | None
    member: MemberReferenceModel | None
    payment_method: PaymentMethodReferenceModel | None
    classification: ClassificationReferenceModel | None
    amount: float | None
    billable_option: BillableOption | None
    date: str | None
    location_id: int | None
    business_unit_id: int | None
    notes: str | None
    agreement: AgreementReferenceModel | None
    invoice_amount: float | None
    mobile_guid: str | None
    taxes: list[ExpenseTaxModel] | None
    invoice: InvoiceReferenceModel | None
    currency: CurrencyReferenceModel | None
    status: Status | None
    bill_amount: float | None
    agreement_amount: float | None
    odometer_start: float | None
    odometer_end: float | None
    ticket: TicketReferenceModel | None
    project: ProjectReferenceModel | None
    phase: ProjectPhaseReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True