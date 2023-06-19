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
from pywise.models.manage.SecurityRoleReferenceModel import SecurityRoleReferenceModel
from pywise.models.manage.StructureReferenceModel import StructureReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
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
from pywise.models.manage.LdapConfigurationReferenceModel import LdapConfigurationReferenceModel
from pywise.models.manage.MemberSsoSettingsReferenceModel import MemberSsoSettingsReferenceModel
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

class MemberModel(ConnectWiseModel):
    id: int
    identifier: str
    password: str
    first_name: str
    middle_initial: str
    last_name: str
    title: str
    report_card: ReportCardReferenceModel
    license_class: LicenseClass
    disable_online_flag: bool
    enable_mobile_flag: bool
    type: MemberTypeReferenceModel
    employee_identifer: str
    vendor_number: str
    notes: str
    time_zone: TimeZoneSetupReferenceModel
    country: CountryReferenceModel
    service_board_team_ids: list[int]
    enable_mobile_gps_flag: bool
    inactive_date: str
    inactive_flag: bool
    last_login: str
    photo: DocumentReferenceModel
    partner_portal_flag: bool
    client_id: str
    sts_user_admin_url: str
    token: str
    toast_notification_flag: bool
    member_personas: list[int]
    office365: MemberOffice365Model
    office_email: str
    office_phone: str
    office_extension: str
    mobile_email: str
    mobile_phone: str
    mobile_extension: str
    home_email: str
    home_phone: str
    home_extension: str
    default_email: DefaultEmail
    primary_email: str
    default_phone: DefaultPhone
    security_role: SecurityRoleReferenceModel
    admin_flag: bool
    structure_level: StructureReferenceModel
    security_location: SystemLocationReferenceModel
    default_location: SystemLocationReferenceModel
    default_department: SystemDepartmentReferenceModel
    reports_to: MemberReferenceModel
    restrict_location_flag: bool
    restrict_department_flag: bool
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    time_approver: MemberReferenceModel
    expense_approver: MemberReferenceModel
    billable_forecast: float
    daily_capacity: float
    hourly_cost: float
    hourly_rate: float
    include_in_utilization_reporting_flag: bool
    require_expense_entry_flag: bool
    require_time_sheet_entry_flag: bool
    require_start_and_end_time_on_time_entry_flag: bool
    allow_in_cell_entry_on_time_sheet: bool
    enter_time_against_company_flag: bool
    allow_expenses_entered_against_companies_flag: bool
    time_reminder_email_flag: bool
    days_tolerance: int
    minimum_hours: float
    time_sheet_start_date: str
    hire_date: str
    service_default_location: SystemLocationReferenceModel
    service_default_department: SystemDepartmentReferenceModel
    service_default_board: BoardReferenceModel
    restrict_service_default_location_flag: bool
    restrict_service_default_department_flag: bool
    excluded_service_board_ids: list[int]
    project_default_location: SystemLocationReferenceModel
    project_default_department: SystemDepartmentReferenceModel
    project_default_board: ProjectBoardReferenceModel
    restrict_project_default_location_flag: bool
    restrict_project_default_department_flag: bool
    excluded_project_board_ids: list[int]
    schedule_default_location: SystemLocationReferenceModel
    schedule_default_department: SystemDepartmentReferenceModel
    schedule_capacity: float
    service_location: ServiceLocationReferenceModel
    restrict_schedule_flag: bool
    hide_member_in_dispatch_portal_flag: bool
    calendar: CalendarReferenceModel
    sales_default_location: SystemLocationReferenceModel
    restrict_default_sales_territory_flag: bool
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    restrict_default_warehouse_flag: bool
    restrict_default_warehouse_bin_flag: bool
    mapi_name: str
    calendar_sync_integration_flag: bool
    enable_ldap_authentication_flag: bool
    ldap_configuration: LdapConfigurationReferenceModel
    ldap_user_name: str
    company_activity_tab_format: CompanyActivityTabFormat
    invoice_time_tab_format: InvoiceTimeTabFormat
    invoice_screen_default_tab_format: InvoiceScreenDefaultTabFormat
    invoicing_display_options: InvoicingDisplayOptions
    agreement_invoicing_display_options: AgreementInvoicingDisplayOptions
    authentication_service_type: AuthenticationServiceType
    timebased_one_time_password_activated: bool
    sso_settings: MemberSsoSettingsReferenceModel
    auto_start_stopwatch: bool
    auto_popup_quick_notes_with_stopwatch: bool
    signature: str
    global_search_default_ticket_filter: GlobalSearchDefaultTicketFilter
    global_search_default_sort: GlobalSearchDefaultSort
    phone_source: str
    phone_integration_type: PhoneIntegrationType
    use_browser_language_flag: bool
    _info: dict[str, str]
    copy_pod_layouts: bool
    copy_shared_default_views: bool
    copy_column_layouts_and_filters: bool
    from_member_rec_id: int
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True