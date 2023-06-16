from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.SLAReferenceModel import SLAReferenceModel
from enum import Enum
from pywise.models.BillingCycleReferenceModel import BillingCycleReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel
class ApplicationUnits(str, Enum):
    Amount = 'Amount'
    Hours = 'Hours'
    Incidents = 'Incidents'
class ApplicationCycle(str, Enum):
    Contract2Weeks = 'Contract2Weeks'
    Contract4Weeks = 'Contract4Weeks'
    ContractYear = 'ContractYear'
    CalendarMonth = 'CalendarMonth'
    CalendarQuarter = 'CalendarQuarter'
    CalendarWeek = 'CalendarWeek'
    ContractQuarter = 'ContractQuarter'
    CalendarYear = 'CalendarYear'
class EmployeeCompRate(str, Enum):
    Actual = 'Actual'
    Hourly = 'Hourly'
class EmployeeCompNotExceed(str, Enum):
    Billing = 'Billing'
    Amount = 'Amount'
    Percent = 'Percent'
class InvoicingCycle(str, Enum):
    ContractYear = 'ContractYear'
    CalendarYear = 'CalendarYear'
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillExpenses(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillProducts(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class PeriodType(str, Enum):
    Current = 'Current'
    Future = 'Future'
    Both = 'Both'
    Undefined = 'Undefined'
class AgreementStatus(str, Enum):
    Active = 'Active'
    Cancelled = 'Cancelled'
    Expired = 'Expired'
    Inactive = 'Inactive'

class AgreementModel(ConnectWiseModel):
    id: int | None
    name: str | None
    type: AgreementTypeReferenceModel | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    site: SiteReferenceModel | None
    sub_contract_company: CompanyReferenceModel | None
    sub_contract_contact: ContactReferenceModel | None
    parent_agreement: AgreementReferenceModel | None
    customer_p_o: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    restrict_location_flag: bool | None
    restrict_department_flag: bool | None
    start_date: str | None
    end_date: str | None
    no_ending_date_flag: bool | None
    opportunity: OpportunityReferenceModel | None
    cancelled_flag: bool | None
    date_cancelled: str | None
    reason_cancelled: str | None
    sla: SLAReferenceModel | None
    work_order: str | None
    internal_notes: str | None
    application_units: ApplicationUnits | None
    application_limit: float | None
    application_cycle: ApplicationCycle | None
    application_unlimited_flag: bool | None
    one_time_flag: bool | None
    cover_agreement_time: bool | None
    cover_agreement_product: bool | None
    cover_agreement_expense: bool | None
    cover_sales_tax: bool | None
    carry_over_unused: bool | None
    allow_overruns: bool | None
    expired_days: int | None
    limit: int | None
    expire_when_zero: bool | None
    charge_to_firm: bool | None
    employee_comp_rate: EmployeeCompRate | None
    employee_comp_not_exceed: EmployeeCompNotExceed | None
    comp_hourly_rate: float | None
    comp_limit_amount: float | None
    billing_cycle: BillingCycleReferenceModel | None
    bill_one_time_flag: bool | None
    billing_terms: BillingTermsReferenceModel | None
    invoicing_cycle: InvoicingCycle | None
    bill_to_company: CompanyReferenceModel | None
    bill_to_contact: ContactReferenceModel | None
    bill_to_site: SiteReferenceModel | None
    bill_amount: float | None
    taxable: bool | None
    prorate_first_bill: float | None
    bill_start_date: str | None
    tax_code: TaxCodeReferenceModel | None
    restrict_down_payment: bool | None
    prorate_flag: bool | None
    invoice_description: str | None
    top_comment: bool | None
    bottom_comment: bool | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    project_type: ProjectTypeReferenceModel | None
    invoice_template: InvoiceTemplateReferenceModel | None
    bill_time: BillTime | None
    bill_expenses: BillExpenses | None
    bill_products: BillProducts | None
    billable_time_invoice: bool | None
    billable_expense_invoice: bool | None
    billable_product_invoice: bool | None
    currency: CurrencyReferenceModel | None
    period_type: PeriodType | None
    auto_invoice_flag: bool | None
    next_invoice_date: str | None
    company_location: SystemLocationReferenceModel | None
    agreement_status: AgreementStatus | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True