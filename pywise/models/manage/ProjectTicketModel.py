from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.manage.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class KnowledgeBaseLinkType(str, Enum):
    Activity = 'Activity'
    ProjectIssue = 'ProjectIssue'
    KnowledgeBaseArticle = 'KnowledgeBaseArticle'
    ProjectTicket = 'ProjectTicket'
    ServiceTicket = 'ServiceTicket'
    Time = 'Time'
class SubBillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
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

class ProjectTicketModel(ConnectWiseModel):
    id: int
    summary: str
    is_issue_flag: bool
    board: BoardReferenceModel
    status: ServiceStatusReferenceModel
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    project: ProjectReferenceModel
    phase: ProjectPhaseReferenceModel
    wbs_code: str
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
    owner: MemberReferenceModel
    priority: PriorityReferenceModel
    service_location: ServiceLocationReferenceModel
    source: ServiceSourceReferenceModel
    required_date: str
    budget_hours: float
    opportunity: OpportunityReferenceModel
    agreement: AgreementReferenceModel
    knowledge_base_category_id: int
    knowledge_base_sub_category_id: int
    knowledge_base_link_id: int
    knowledge_base_link_type: KnowledgeBaseLinkType
    allow_all_clients_portal_view: bool
    customer_updated_flag: bool
    automatic_email_contact_flag: bool
    automatic_email_resource_flag: bool
    automatic_email_cc_flag: bool
    automatic_email_cc: str
    closed_date: str
    closed_by: str
    closed_flag: bool
    actual_hours: float
    approved: bool
    sub_billing_method: SubBillingMethod
    sub_billing_amount: float
    sub_date_accepted: str
    resources: str
    bill_time: BillTime
    bill_expenses: BillExpenses
    bill_products: BillProducts
    predecessor_type: PredecessorType
    predecessor_id: int
    predecessor_closed_flag: bool
    lag_days: int
    lag_nonworking_days_flag: bool
    estimated_start_date: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    duration: int
    mobile_guid: str
    currency: CurrencyReferenceModel
    _info: dict[str, str]
    initial_description: str
    initial_internal_analysis: str
    initial_resolution: str
    contact_email_lookup: str
    process_notifications: bool
    skip_callback: bool
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True