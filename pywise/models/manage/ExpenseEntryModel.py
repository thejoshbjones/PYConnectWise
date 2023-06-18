from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ExpenseReportReferenceModel import ExpenseReportReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from enum import Enum
from pywise.models.manage.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.PaymentMethodReferenceModel import PaymentMethodReferenceModel
from pywise.models.manage.ClassificationReferenceModel import ClassificationReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.ExpenseTaxModel import ExpenseTaxModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
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