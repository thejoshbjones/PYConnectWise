from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.ProjectStatusReferenceModel import ProjectStatusReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel
class BillExpenses(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
class BillingRateType(str, Enum):
    StaffMember = 'StaffMember'
    WorkRole = 'WorkRole'
class BillProducts(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BudgetAnalysis(str, Enum):
    ActualHours = 'ActualHours'
    BillableHours = 'BillableHours'

class ProjectModel(ConnectWiseModel):
    id: int | None
    _info: dict[str, str] | None
    actual_end: str | None
    actual_hours: float | None
    actual_start: str | None
    agreement: AgreementReferenceModel | None
    bill_expenses: BillExpenses | None
    billing_amount: float | None
    billing_attention: str | None
    billing_method: BillingMethod | None
    billing_rate_type: BillingRateType | None
    billing_terms: BillingTermsReferenceModel | None
    bill_products: BillProducts | None
    bill_project_after_closed_flag: bool | None
    bill_time: BillTime | None
    bill_to_company: CompanyReferenceModel | None
    bill_to_contact: ContactReferenceModel | None
    bill_to_site: SiteReferenceModel | None
    bill_unapproved_time_and_expense: bool | None
    board: ProjectBoardReferenceModel | None
    budget_analysis: BudgetAnalysis | None
    budget_flag: bool | None
    budget_hours: float | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    customer_p_o: str | None
    description: str | None
    currency: CurrencyReferenceModel | None
    downpayment: float | None
    estimated_end: str | None
    percent_complete: float | None
    estimated_expense_revenue: float | None
    estimated_hours: float | None
    estimated_product_revenue: float | None
    estimated_start: str | None
    estimated_time_revenue: float | None
    expense_approver: MemberReferenceModel | None
    include_dependencies_flag: bool | None
    include_estimates_flag: bool | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    manager: MemberReferenceModel | None
    name: str | None
    opportunity: OpportunityReferenceModel | None
    project_template_id: int | None
    restrict_down_payment_flag: bool | None
    scheduled_end: str | None
    scheduled_hours: float | None
    scheduled_start: str | None
    ship_to_company: CompanyReferenceModel | None
    ship_to_contact: ContactReferenceModel | None
    ship_to_site: SiteReferenceModel | None
    site: SiteReferenceModel | None
    status: ProjectStatusReferenceModel | None
    closed_flag: bool | None
    time_approver: MemberReferenceModel | None
    type: ProjectTypeReferenceModel | None
    do_not_display_in_portal_flag: bool | None
    billing_start_date: str | None
    estimated_time_cost: float | None
    estimated_expense_cost: float | None
    estimated_product_cost: float | None
    tax_code: TaxCodeReferenceModel | None
    company_location: SystemLocationReferenceModel | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True