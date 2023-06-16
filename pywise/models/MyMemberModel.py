from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ReportCardReferenceModel import ReportCardReferenceModel
from enum import Enum
from pywise.models.MemberTypeReferenceModel import MemberTypeReferenceModel
from pywise.models.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from pywise.models.DocumentReferenceModel import DocumentReferenceModel
from pywise.models.SecurityRoleReferenceModel import SecurityRoleReferenceModel
from pywise.models.StructureReferenceModel import StructureReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.LdapConfigurationReferenceModel import LdapConfigurationReferenceModel
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

class MyMemberModel(ConnectWiseModel):
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
    toast_notification_flag: bool | None
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
    default_phone: DefaultPhone | None
    security_role: SecurityRoleReferenceModel | None
    admin_flag: bool | None
    structure_level: StructureReferenceModel | None
    security_location: SystemLocationReferenceModel | None
    default_location: SystemLocationReferenceModel | None
    default_department: SystemDepartmentReferenceModel | None
    reports_to: MemberReferenceModel | None
    restrict_location_flag: bool | None
    restrict_department_flag: bool | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    time_approver: MemberReferenceModel | None
    expense_approver: MemberReferenceModel | None
    billable_forecast: float | None
    daily_capacity: float | None
    hourly_cost: float | None
    hourly_rate: float | None
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
    restrict_service_default_location_flag: bool | None
    restrict_service_default_department_flag: bool | None
    excluded_service_board_ids: list[int] | None
    project_default_location: SystemLocationReferenceModel | None
    project_default_department: SystemDepartmentReferenceModel | None
    project_default_board: ProjectBoardReferenceModel | None
    restrict_project_default_location_flag: bool | None
    restrict_project_default_department_flag: bool | None
    excluded_project_board_ids: list[int] | None
    schedule_default_location: SystemLocationReferenceModel | None
    schedule_default_department: SystemDepartmentReferenceModel | None
    schedule_capacity: float | None
    service_location: ServiceLocationReferenceModel | None
    restrict_schedule_flag: bool | None
    hide_member_in_dispatch_portal_flag: bool | None
    calendar: CalendarReferenceModel | None
    sales_default_location: SystemLocationReferenceModel | None
    restrict_default_sales_territory_flag: bool | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    restrict_default_warehouse_flag: bool | None
    restrict_default_warehouse_bin_flag: bool | None
    mapi_name: str | None
    calendar_sync_integration_flag: bool | None
    enable_ldap_authentication_flag: bool | None
    ldap_configuration: LdapConfigurationReferenceModel | None
    ldap_user_name: str | None
    company_activity_tab_format: CompanyActivityTabFormat | None
    invoice_time_tab_format: InvoiceTimeTabFormat | None
    invoice_screen_default_tab_format: InvoiceScreenDefaultTabFormat | None
    invoicing_display_options: InvoicingDisplayOptions | None
    agreement_invoicing_display_options: AgreementInvoicingDisplayOptions | None
    corelytics_username: str | None
    corelytics_password: str | None
    authentication_service_type: AuthenticationServiceType | None
    timebased_one_time_password_activated: bool | None
    sso_session_flag: bool | None
    sso_client_id: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True