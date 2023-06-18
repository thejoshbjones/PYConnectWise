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
    id: int | None
    summary: str | None
    is_issue_flag: bool | None
    board: BoardReferenceModel | None
    status: ServiceStatusReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    project: ProjectReferenceModel | None
    phase: ProjectPhaseReferenceModel | None
    wbs_code: str | None
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
    owner: MemberReferenceModel | None
    priority: PriorityReferenceModel | None
    service_location: ServiceLocationReferenceModel | None
    source: ServiceSourceReferenceModel | None
    required_date: str | None
    budget_hours: float | None
    opportunity: OpportunityReferenceModel | None
    agreement: AgreementReferenceModel | None
    knowledge_base_category_id: int | None
    knowledge_base_sub_category_id: int | None
    knowledge_base_link_id: int | None
    knowledge_base_link_type: KnowledgeBaseLinkType | None
    allow_all_clients_portal_view: bool | None
    customer_updated_flag: bool | None
    automatic_email_contact_flag: bool | None
    automatic_email_resource_flag: bool | None
    automatic_email_cc_flag: bool | None
    automatic_email_cc: str | None
    closed_date: str | None
    closed_by: str | None
    closed_flag: bool | None
    actual_hours: float | None
    approved: bool | None
    sub_billing_method: SubBillingMethod | None
    sub_billing_amount: float | None
    sub_date_accepted: str | None
    resources: str | None
    bill_time: BillTime | None
    bill_expenses: BillExpenses | None
    bill_products: BillProducts | None
    predecessor_type: PredecessorType | None
    predecessor_id: int | None
    predecessor_closed_flag: bool | None
    lag_days: int | None
    lag_nonworking_days_flag: bool | None
    estimated_start_date: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    duration: int | None
    mobile_guid: str | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None
    initial_description: str | None
    initial_internal_analysis: str | None
    initial_resolution: str | None
    contact_email_lookup: str | None
    process_notifications: bool | None
    skip_callback: bool | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True