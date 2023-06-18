from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ServiceSignoffReferenceModel import ServiceSignoffReferenceModel
from pywise.models.ServiceEmailTemplateReferenceModel import ServiceEmailTemplateReferenceModel
from pywise.models.ServiceEmailTemplateReferenceModel import ServiceEmailTemplateReferenceModel
from pywise.models.DocumentReferenceModel import DocumentReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from enum import Enum
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
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
    id: int | None
    name: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    inactive_flag: bool | None
    sign_off_template: ServiceSignoffReferenceModel | None
    send_to_contact_flag: bool | None
    contact_template: ServiceEmailTemplateReferenceModel | None
    send_to_resource_flag: bool | None
    resource_template: ServiceEmailTemplateReferenceModel | None
    project_flag: bool | None
    show_dependencies_flag: bool | None
    show_estimates_flag: bool | None
    board_icon: DocumentReferenceModel | None
    bill_tickets_after_closed_flag: bool | None
    bill_ticket_separately_flag: bool | None
    bill_unapproved_time_expense_flag: bool | None
    override_billing_setup_flag: bool | None
    dispatch_member: MemberReferenceModel | None
    service_manager_member: MemberReferenceModel | None
    duty_manager_member: MemberReferenceModel | None
    oncall_member: MemberReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    bill_time: BillTime | None
    bill_expense: BillExpense | None
    bill_product: BillProduct | None
    auto_close_status: ServiceStatusReferenceModel | None
    auto_assign_new_tickets_flag: bool | None
    auto_assign_new_e_c_tickets_flag: bool | None
    auto_assign_new_portal_tickets_flag: bool | None
    discussions_locked_flag: bool | None
    time_entry_locked_flag: bool | None
    notify_email_from: str | None
    notify_email_from_name: str | None
    closed_loop_discussions_flag: bool | None
    closed_loop_resolution_flag: bool | None
    closed_loop_internal_analysis_flag: bool | None
    time_entry_discussion_flag: bool | None
    time_entry_resolution_flag: bool | None
    time_entry_internal_analysis_flag: bool | None
    problem_sort: ProblemSort | None
    resolution_sort: ResolutionSort | None
    internal_analysis_sort: InternalAnalysisSort | None
    email_connector_allow_reopen_closed_flag: bool | None
    email_connector_reopen_status: ServiceStatusReferenceModel | None
    email_connector_reopen_resources_flag: bool | None
    email_connector_new_ticket_no_match_flag: bool | None
    email_connector_never_reopen_by_days_flag: bool | None
    email_connector_reopen_days_limit: int | None
    email_connector_never_reopen_by_days_closed_flag: bool | None
    email_connector_reopen_days_closed_limit: int | None
    use_member_display_name_flag: bool | None
    send_to_c_c_flag: bool | None
    auto_assign_ticket_owner_flag: bool | None
    closed_loop_all_flag: bool | None
    percentage_calculation: PercentageCalculation | None
    all_sort: AllSort | None
    mark_first_note_issue_flag: bool | None
    restrict_board_by_default_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True