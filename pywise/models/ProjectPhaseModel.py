from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.PhaseStatusReferenceModel import PhaseStatusReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from enum import Enum
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel
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
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'

class ProjectPhaseModel(ConnectWiseModel):
    id: int | None
    project_id: int | None
    description: str | None
    board: ProjectBoardReferenceModel | None
    status: PhaseStatusReferenceModel | None
    agreement: AgreementReferenceModel | None
    opportunity: OpportunityReferenceModel | None
    parent_phase: ProjectPhaseReferenceModel | None
    wbs_code: str | None
    bill_time: BillTime | None
    bill_expenses: BillExpenses | None
    bill_products: BillProducts | None
    mark_as_milestone_flag: bool | None
    notes: str | None
    deadline_date: str | None
    bill_separately_flag: bool | None
    billing_method: BillingMethod | None
    scheduled_hours: float | None
    scheduled_start: str | None
    scheduled_end: str | None
    actual_hours: float | None
    actual_start: str | None
    actual_end: str | None
    budget_hours: float | None
    location_id: int | None
    business_unit_id: int | None
    hourly_rate: float | None
    billing_start_date: str | None
    bill_phase_closed_flag: bool | None
    bill_project_closed_flag: bool | None
    downpayment: float | None
    po_number: str | None
    po_amount: float | None
    estimated_time_cost: float | None
    estimated_expense_cost: float | None
    estimated_product_cost: float | None
    estimated_time_revenue: float | None
    estimated_expense_revenue: float | None
    estimated_product_revenue: float | None
    currency: CurrencyReferenceModel | None
    bill_to_company: CompanyReferenceModel | None
    bill_to_contact: ContactReferenceModel | None
    bill_to_site: SiteReferenceModel | None
    ship_to_company: CompanyReferenceModel | None
    ship_to_contact: ContactReferenceModel | None
    ship_to_site: SiteReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True