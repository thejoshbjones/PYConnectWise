from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ReportCardReferenceModel import ReportCardReferenceModel
from enum import Enum
from pywise.models.manage.MemberTypeReferenceModel import MemberTypeReferenceModel
from pywise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.DocumentReferenceModel import DocumentReferenceModel
from pywise.models.manage.MemberOffice365Model import MemberOffice365Model
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class LicenseClass(str, Enum):
    A = 'A'
    C = 'C'
    F = 'F'
    X = 'X'
class DefaultEmail(str, Enum):
    Office = 'Office'
    Mobile = 'Mobile'
    Home = 'Home'
class DefaultPhone(str, Enum):
    Office = 'Office'
    Mobile = 'Mobile'
    Home = 'Home'
class CompanyActivityTabFormat(str, Enum):
    SummaryList = 'SummaryList'
    DetailList = 'DetailList'
class InvoiceTimeTabFormat(str, Enum):
    SummaryList = 'SummaryList'
    DetailList = 'DetailList'
class InvoiceScreenDefaultTabFormat(str, Enum):
    ShowInvoicingTab = 'ShowInvoicingTab'
    ShowAgreementInvoicingTab = 'ShowAgreementInvoicingTab'
class InvoicingDisplayOptions(str, Enum):
    RemainOnInvoicingScreen = 'RemainOnInvoicingScreen'
    ShowRecentInvoices = 'ShowRecentInvoices'
class AgreementInvoicingDisplayOptions(str, Enum):
    RemainOnInvoicingScreen = 'RemainOnInvoicingScreen'
    ShowRecentInvoices = 'ShowRecentInvoices'
class AuthenticationServiceType(str, Enum):
    AuthAnvil = 'AuthAnvil'
    GoogleAuthenticator = 'GoogleAuthenticator'
    Email = 'Email'
class GlobalSearchDefaultTicketFilter(str, Enum):
    OpenRecords = 'OpenRecords'
    ClosedRecords = 'ClosedRecords'
    AllRecords = 'AllRecords'
class GlobalSearchDefaultSort(str, Enum):
    NONE = 'NONE'
    LastUpdatedDesc = 'LastUpdatedDesc'
    LastUpdatedAsc = 'LastUpdatedAsc'
    CreatedDesc = 'CreatedDesc'
    CreatedAsc = 'CreatedAsc'
class PhoneIntegrationType(str, Enum):
    TAPI = 'TAPI'
    SKYPE = 'SKYPE'
    NONE = 'NONE'

class MyAccountModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    password: str | None
    first_name: str | None
    middle_initial: str | None
    last_name: str | None
    title: str | None
    report_card: ReportCardReferenceModel | None
    license_class: LicenseClass | None
    disable_online_flag: bool | None
    enable_mobile_flag: bool | None
    type: MemberTypeReferenceModel | None
    employee_identifer: str | None
    vendor_number: str | None
    notes: str | None
    time_zone: TimeZoneSetupReferenceModel | None
    country: CountryReferenceModel | None
    service_board_team_ids: list[int] | None
    enable_mobile_gps_flag: bool | None
    inactive_date: str | None
    inactive_flag: bool | None
    last_login: str | None
    photo: DocumentReferenceModel | None
    partner_portal_flag: bool | None
    client_id: str | None
    sts_user_admin_url: str | None
    token: str | None
    toast_notification_flag: bool | None
    member_personas: list[int] | None
    office365: MemberOffice365Model | None
    office_email: str | None
    office_phone: str | None
    office_extension: str | None
    mobile_email: str | None
    mobile_phone: str | None
    mobile_extension: str | None
    home_email: str | None
    home_phone: str | None
    home_extension: str | None
    default_email: DefaultEmail | None
    primary_email: str | None
    default_phone: DefaultPhone | None
    default_location: SystemLocationReferenceModel | None
    default_department: SystemDepartmentReferenceModel | None
    reports_to: MemberReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    time_approver: MemberReferenceModel | None
    expense_approver: MemberReferenceModel | None
    billable_forecast: float | None
    daily_capacity: float | None
    include_in_utilization_reporting_flag: bool | None
    require_expense_entry_flag: bool | None
    require_time_sheet_entry_flag: bool | None
    require_start_and_end_time_on_time_entry_flag: bool | None
    allow_in_cell_entry_on_time_sheet: bool | None
    enter_time_against_company_flag: bool | None
    allow_expenses_entered_against_companies_flag: bool | None
    time_reminder_email_flag: bool | None
    days_tolerance: int | None
    minimum_hours: float | None
    time_sheet_start_date: str | None
    hire_date: str | None
    service_default_location: SystemLocationReferenceModel | None
    service_default_department: SystemDepartmentReferenceModel | None
    service_default_board: BoardReferenceModel | None
    project_default_location: SystemLocationReferenceModel | None
    project_default_department: SystemDepartmentReferenceModel | None
    project_default_board: ProjectBoardReferenceModel | None
    schedule_default_location: SystemLocationReferenceModel | None
    schedule_default_department: SystemDepartmentReferenceModel | None
    schedule_capacity: float | None
    service_location: ServiceLocationReferenceModel | None
    hide_member_in_dispatch_portal_flag: bool | None
    calendar: CalendarReferenceModel | None
    sales_default_location: SystemLocationReferenceModel | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    mapi_name: str | None
    calendar_sync_integration_flag: bool | None
    company_activity_tab_format: CompanyActivityTabFormat | None
    invoice_time_tab_format: InvoiceTimeTabFormat | None
    invoice_screen_default_tab_format: InvoiceScreenDefaultTabFormat | None
    invoicing_display_options: InvoicingDisplayOptions | None
    agreement_invoicing_display_options: AgreementInvoicingDisplayOptions | None
    authentication_service_type: AuthenticationServiceType | None
    timebased_one_time_password_activated: bool | None
    auto_start_stopwatch: bool | None
    auto_popup_quick_notes_with_stopwatch: bool | None
    signature: str | None
    global_search_default_ticket_filter: GlobalSearchDefaultTicketFilter | None
    global_search_default_sort: GlobalSearchDefaultSort | None
    phone_source: str | None
    phone_integration_type: PhoneIntegrationType | None
    use_browser_language_flag: bool | None
    _info: dict[str, str] | None
    copy_pod_layouts: bool | None
    copy_shared_default_views: bool | None
    copy_column_layouts_and_filters: bool | None
    from_member_rec_id: int | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True