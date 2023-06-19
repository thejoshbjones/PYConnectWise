from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
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
    id: int
    name: str
    board: BoardReferenceModel
    type: ServiceTypeReferenceModel
    item: ServiceItemReferenceModel
    subtype: ServiceSubTypeReferenceModel
    service_location: ServiceLocationReferenceModel
    status: ServiceStatusReferenceModel
    source: ServiceSourceReferenceModel
    priority: PriorityReferenceModel
    team: ServiceTeamReferenceModel
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    assigned_notify_flag: bool
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    summary: str
    problem: str
    hours_budget: float
    internal_analysis: str
    time_billable_flag: bool
    expense_billable_flag: bool
    purchase_order_number: str
    reference: str
    bill_complete__flag: bool
    bill_service_separately_flag: bool
    billing_amount: float
    bill_unapproved_time_and_expenses_flag: bool
    override_flag: bool
    time_invoice_flag: bool
    expense_invoice_flag: bool
    product_invoice_flag: bool
    agreement: AgreementReferenceModel
    billing_method: BillingMethod
    severity: Severity
    impact: Impact
    assigned_by: MemberReferenceModel
    schedule_days_before: int
    service_days_before: int
    attach_schedule_to_new_service_flag: bool
    template_flag: bool
    email_contact_flag: bool
    email_resource_flag: bool
    email_c_c_flag: bool
    email_c_c: str
    restrict_downpayment_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True