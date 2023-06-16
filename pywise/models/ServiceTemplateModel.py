from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
class Severity(str, Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
class Impact(str, Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'

class ServiceTemplateModel(ConnectWiseModel):
    id: int | None
    name: str | None
    board: BoardReferenceModel | None
    type: ServiceTypeReferenceModel | None
    item: ServiceItemReferenceModel | None
    subtype: ServiceSubTypeReferenceModel | None
    service_location: ServiceLocationReferenceModel | None
    status: ServiceStatusReferenceModel | None
    source: ServiceSourceReferenceModel | None
    priority: PriorityReferenceModel | None
    team: ServiceTeamReferenceModel | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    site: SiteReferenceModel | None
    assigned_notify_flag: bool | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    summary: str | None
    problem: str | None
    hours_budget: float | None
    internal_analysis: str | None
    time_billable_flag: bool | None
    expense_billable_flag: bool | None
    purchase_order_number: str | None
    reference: str | None
    bill_complete__flag: bool | None
    bill_service_separately_flag: bool | None
    billing_amount: float | None
    bill_unapproved_time_and_expenses_flag: bool | None
    override_flag: bool | None
    time_invoice_flag: bool | None
    expense_invoice_flag: bool | None
    product_invoice_flag: bool | None
    agreement: AgreementReferenceModel | None
    billing_method: BillingMethod | None
    severity: Severity | None
    impact: Impact | None
    assigned_by: MemberReferenceModel | None
    schedule_days_before: int | None
    service_days_before: int | None
    attach_schedule_to_new_service_flag: bool | None
    template_flag: bool | None
    email_contact_flag: bool | None
    email_resource_flag: bool | None
    email_c_c_flag: bool | None
    email_c_c: str | None
    restrict_downpayment_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True