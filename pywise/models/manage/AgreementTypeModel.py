from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.SLAReferenceModel import SLAReferenceModel
from pywise.models.manage.BillingCycleReferenceModel import BillingCycleReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.manage.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pywise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.manage.EmailTemplateReferenceModel import EmailTemplateReferenceModel
class PrefixSuffixOption(str, Enum):
    Prefix = 'Prefix'
    Suffix = 'Suffix'
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

class AgreementTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    prefix_suffix_option: PrefixSuffixOption | None
    default_flag: bool | None
    inactive_flag: bool | None
    pre_payment_flag: bool | None
    invoice_pre_suffix: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    restrict_location_flag: bool | None
    restrict_department_flag: bool | None
    sla: SLAReferenceModel | None
    application_units: ApplicationUnits | None
    application_limit: float | None
    application_cycle: ApplicationCycle | None
    application_unlimited_flag: bool | None
    one_time_flag: bool | None
    cover_agreement_time_flag: bool | None
    cover_agreement_product_flag: bool | None
    cover_agreement_expense_flag: bool | None
    cover_sales_tax_flag: bool | None
    carry_over_unused_flag: bool | None
    allow_overruns_flag: bool | None
    expired_days: int | None
    limit: int | None
    expire_when_zero: bool | None
    charge_to_firm_flag: bool | None
    employee_comp_rate: EmployeeCompRate | None
    employee_comp_not_exceed: EmployeeCompNotExceed | None
    comp_hourly_rate: float | None
    comp_limit_amount: float | None
    billing_cycle: BillingCycleReferenceModel | None
    bill_one_time_flag: bool | None
    billing_terms: BillingTermsReferenceModel | None
    invoicing_cycle: InvoicingCycle | None
    bill_amount: float | None
    taxable_flag: bool | None
    restrict_down_payment_flag: bool | None
    invoice_description: str | None
    top_comment_flag: bool | None
    bottom_comment_flag: bool | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    project_type: ProjectTypeReferenceModel | None
    invoice_template: InvoiceTemplateReferenceModel | None
    bill_time: BillTime | None
    bill_expenses: BillExpenses | None
    bill_products: BillProducts | None
    billable_time_invoice_flag: bool | None
    billable_expense_invoice_flag: bool | None
    billable_product_invoice_flag: bool | None
    copy_work_roles_flag: bool | None
    copy_work_types_flag: bool | None
    exclusion_work_role_ids: list[int] | None
    add_all_work_role_exclusions: bool | None
    remove_all_work_role_exclusions: bool | None
    exclusion_work_type_ids: list[int] | None
    add_all_work_type_exclusions: bool | None
    remove_all_work_type_exclusions: bool | None
    integration_x_ref: str | None
    prorate_flag: bool | None
    email_template: EmailTemplateReferenceModel | None
    auto_invoice_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True