from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.ServiceSignoffReferenceModel import ServiceSignoffReferenceModel
from pywise.models.manage.ServiceEmailTemplateReferenceModel import ServiceEmailTemplateReferenceModel
from pywise.models.manage.ServiceEmailTemplateReferenceModel import ServiceEmailTemplateReferenceModel
from pywise.models.manage.DocumentReferenceModel import DocumentReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from enum import Enum
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillExpense(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillProduct(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class ProblemSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class ResolutionSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class InternalAnalysisSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class PercentageCalculation(str, Enum):
    ActualHours = 'ActualHours'
    Manual = 'Manual'
    ClosedPhases = 'ClosedPhases'
    ClosedTickets = 'ClosedTickets'
class AllSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'

class BoardModel(ConnectWiseModel):
    id: int
    name: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    inactive_flag: bool
    sign_off_template: ServiceSignoffReferenceModel
    send_to_contact_flag: bool
    contact_template: ServiceEmailTemplateReferenceModel
    send_to_resource_flag: bool
    resource_template: ServiceEmailTemplateReferenceModel
    project_flag: bool
    show_dependencies_flag: bool
    show_estimates_flag: bool
    board_icon: DocumentReferenceModel
    bill_tickets_after_closed_flag: bool
    bill_ticket_separately_flag: bool
    bill_unapproved_time_expense_flag: bool
    override_billing_setup_flag: bool
    dispatch_member: MemberReferenceModel
    service_manager_member: MemberReferenceModel
    duty_manager_member: MemberReferenceModel
    oncall_member: MemberReferenceModel
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    bill_time: BillTime
    bill_expense: BillExpense
    bill_product: BillProduct
    auto_close_status: ServiceStatusReferenceModel
    auto_assign_new_tickets_flag: bool
    auto_assign_new_e_c_tickets_flag: bool
    auto_assign_new_portal_tickets_flag: bool
    discussions_locked_flag: bool
    time_entry_locked_flag: bool
    notify_email_from: str
    notify_email_from_name: str
    closed_loop_discussions_flag: bool
    closed_loop_resolution_flag: bool
    closed_loop_internal_analysis_flag: bool
    time_entry_discussion_flag: bool
    time_entry_resolution_flag: bool
    time_entry_internal_analysis_flag: bool
    problem_sort: ProblemSort
    resolution_sort: ResolutionSort
    internal_analysis_sort: InternalAnalysisSort
    email_connector_allow_reopen_closed_flag: bool
    email_connector_reopen_status: ServiceStatusReferenceModel
    email_connector_reopen_resources_flag: bool
    email_connector_new_ticket_no_match_flag: bool
    email_connector_never_reopen_by_days_flag: bool
    email_connector_reopen_days_limit: int
    email_connector_never_reopen_by_days_closed_flag: bool
    email_connector_reopen_days_closed_limit: int
    use_member_display_name_flag: bool
    send_to_c_c_flag: bool
    auto_assign_ticket_owner_flag: bool
    closed_loop_all_flag: bool
    percentage_calculation: PercentageCalculation
    all_sort: AllSort
    mark_first_note_issue_flag: bool
    restrict_board_by_default_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True