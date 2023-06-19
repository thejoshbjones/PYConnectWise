from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.manage.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.manage.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.SLAReferenceModel import SLAReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class RecordType(str, Enum):
    ProjectIssue = 'ProjectIssue'
    ProjectTicket = 'ProjectTicket'
    ServiceTicket = 'ServiceTicket'
class Severity(str, Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
class Impact(str, Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
class SubBillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
class KnowledgeBaseLinkType(str, Enum):
    Activity = 'Activity'
    ProjectIssue = 'ProjectIssue'
    KnowledgeBaseArticle = 'KnowledgeBaseArticle'
    ProjectTicket = 'ProjectTicket'
    ServiceTicket = 'ServiceTicket'
    Time = 'Time'
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
class PredecessorType(str, Enum):
    Ticket = 'Ticket'
    Phase = 'Phase'

class TicketModel(ConnectWiseModel):
    id: int
    summary: str
    record_type: RecordType
    board: BoardReferenceModel
    status: ServiceStatusReferenceModel
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    company: CompanyReferenceModel
    site: SiteReferenceModel
    site_name: str
    address_line1: str
    address_line2: str
    city: str
    state_identifier: str
    zip: str
    country: CountryReferenceModel
    contact: ContactReferenceModel
    contact_name: str
    contact_phone_number: str
    contact_phone_extension: str
    contact_email_address: str
    type: ServiceTypeReferenceModel
    sub_type: ServiceSubTypeReferenceModel
    item: ServiceItemReferenceModel
    team: ServiceTeamReferenceModel
    owner: MemberReferenceModel
    priority: PriorityReferenceModel
    service_location: ServiceLocationReferenceModel
    source: ServiceSourceReferenceModel
    required_date: str
    budget_hours: float
    opportunity: OpportunityReferenceModel
    agreement: AgreementReferenceModel
    severity: Severity
    impact: Impact
    external_x_ref: str
    po_number: str
    knowledge_base_category_id: int
    knowledge_base_sub_category_id: int
    allow_all_clients_portal_view: bool
    customer_updated_flag: bool
    automatic_email_contact_flag: bool
    automatic_email_resource_flag: bool
    automatic_email_cc_flag: bool
    automatic_email_cc: str
    initial_description: str
    initial_internal_analysis: str
    initial_resolution: str
    initial_description_from: str
    contact_email_lookup: str
    process_notifications: bool
    skip_callback: bool
    closed_date: str
    closed_by: str
    closed_flag: bool
    actual_hours: float
    approved: bool
    estimated_expense_cost: float
    estimated_expense_revenue: float
    estimated_product_cost: float
    estimated_product_revenue: float
    estimated_time_cost: float
    estimated_time_revenue: float
    billing_method: BillingMethod
    billing_amount: float
    hourly_rate: float
    sub_billing_method: SubBillingMethod
    sub_billing_amount: float
    sub_date_accepted: str
    date_resolved: str
    date_resplan: str
    date_responded: str
    resolve_minutes: int
    res_plan_minutes: int
    respond_minutes: int
    is_in_sla: bool
    knowledge_base_link_id: int
    resources: str
    parent_ticket_id: int
    has_child_ticket: bool
    has_merged_child_ticket_flag: bool
    knowledge_base_link_type: KnowledgeBaseLinkType
    bill_time: BillTime
    bill_expenses: BillExpenses
    bill_products: BillProducts
    predecessor_type: PredecessorType
    predecessor_id: int
    predecessor_closed_flag: bool
    lag_days: int
    lag_nonworking_days_flag: bool
    estimated_start_date: str
    duration: int
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    mobile_guid: str
    sla: SLAReferenceModel
    sla_status: str
    currency: CurrencyReferenceModel
    merged_parent_ticket: TicketReferenceModel
    integrator_tags: list[str]
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True