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
    id: int
    expense_report: ExpenseReportReferenceModel
    company: CompanyReferenceModel
    charge_to_id: int
    charge_to_type: ChargeToType
    type: ExpenseTypeReferenceModel
    member: MemberReferenceModel
    payment_method: PaymentMethodReferenceModel
    classification: ClassificationReferenceModel
    amount: float
    billable_option: BillableOption
    date: str
    location_id: int
    business_unit_id: int
    notes: str
    agreement: AgreementReferenceModel
    invoice_amount: float
    mobile_guid: str
    taxes: list[ExpenseTaxModel]
    invoice: InvoiceReferenceModel
    currency: CurrencyReferenceModel
    status: Status
    bill_amount: float
    agreement_amount: float
    odometer_start: float
    odometer_end: float
    ticket: TicketReferenceModel
    project: ProjectReferenceModel
    phase: ProjectPhaseReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True