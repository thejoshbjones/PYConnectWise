from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.SLAReferenceModel import SLAReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.TicketReferenceModel import TicketReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel
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
    id: int | None
    summary: str | None
    record_type: RecordType | None
    board: BoardReferenceModel | None
    status: ServiceStatusReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    company: CompanyReferenceModel | None
    site: SiteReferenceModel | None
    site_name: str | None
    address_line1: str | None
    address_line2: str | None
    city: str | None
    state_identifier: str | None
    zip: str | None
    country: CountryReferenceModel | None
    contact: ContactReferenceModel | None
    contact_name: str | None
    contact_phone_number: str | None
    contact_phone_extension: str | None
    contact_email_address: str | None
    type: ServiceTypeReferenceModel | None
    sub_type: ServiceSubTypeReferenceModel | None
    item: ServiceItemReferenceModel | None
    team: ServiceTeamReferenceModel | None
    owner: MemberReferenceModel | None
    priority: PriorityReferenceModel | None
    service_location: ServiceLocationReferenceModel | None
    source: ServiceSourceReferenceModel | None
    required_date: str | None
    budget_hours: float | None
    opportunity: OpportunityReferenceModel | None
    agreement: AgreementReferenceModel | None
    severity: Severity | None
    impact: Impact | None
    external_x_ref: str | None
    po_number: str | None
    knowledge_base_category_id: int | None
    knowledge_base_sub_category_id: int | None
    allow_all_clients_portal_view: bool | None
    customer_updated_flag: bool | None
    automatic_email_contact_flag: bool | None
    automatic_email_resource_flag: bool | None
    automatic_email_cc_flag: bool | None
    automatic_email_cc: str | None
    initial_description: str | None
    initial_internal_analysis: str | None
    initial_resolution: str | None
    initial_description_from: str | None
    contact_email_lookup: str | None
    process_notifications: bool | None
    skip_callback: bool | None
    closed_date: str | None
    closed_by: str | None
    closed_flag: bool | None
    actual_hours: float | None
    approved: bool | None
    estimated_expense_cost: float | None
    estimated_expense_revenue: float | None
    estimated_product_cost: float | None
    estimated_product_revenue: float | None
    estimated_time_cost: float | None
    estimated_time_revenue: float | None
    billing_method: BillingMethod | None
    billing_amount: float | None
    hourly_rate: float | None
    sub_billing_method: SubBillingMethod | None
    sub_billing_amount: float | None
    sub_date_accepted: str | None
    date_resolved: str | None
    date_resplan: str | None
    date_responded: str | None
    resolve_minutes: int | None
    res_plan_minutes: int | None
    respond_minutes: int | None
    is_in_sla: bool | None
    knowledge_base_link_id: int | None
    resources: str | None
    parent_ticket_id: int | None
    has_child_ticket: bool | None
    has_merged_child_ticket_flag: bool | None
    knowledge_base_link_type: KnowledgeBaseLinkType | None
    bill_time: BillTime | None
    bill_expenses: BillExpenses | None
    bill_products: BillProducts | None
    predecessor_type: PredecessorType | None
    predecessor_id: int | None
    predecessor_closed_flag: bool | None
    lag_days: int | None
    lag_nonworking_days_flag: bool | None
    estimated_start_date: str | None
    duration: int | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    mobile_guid: str | None
    sla: SLAReferenceModel | None
    sla_status: str | None
    currency: CurrencyReferenceModel | None
    merged_parent_ticket: TicketReferenceModel | None
    integrator_tags: list[str] | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True