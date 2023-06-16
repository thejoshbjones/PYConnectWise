from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.DocumentReferenceModel import DocumentReferenceModel
from enum import Enum
from pywise.models.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
class LicenseClass(str, Enum):
    A = 'A'
    C = 'C'
    F = 'F'
    X = 'X'

class MyMemberInfoModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    first_name: str | None
    middle_initial: str | None
    last_name: str | None
    full_name: str | None
    default_email: str | None
    photo: DocumentReferenceModel | None
    license_class: LicenseClass | None
    inactive_flag: bool | None
    time_zone: TimeZoneSetupReferenceModel | None
    use_browser_language_flag: bool | None
    default_location: SystemLocationReferenceModel | None
    default_department: SystemDepartmentReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    daily_capacity: float | None
    require_expense_entry_flag: bool | None
    require_time_sheet_entry_flag: bool | None
    require_start_and_end_time_on_time_entry_flag: bool | None
    enter_time_against_company_flag: bool | None
    allow_expenses_entered_against_companies_flag: bool | None
    service_default_board: BoardReferenceModel | None
    service_default_location: SystemLocationReferenceModel | None
    service_default_department: SystemDepartmentReferenceModel | None
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
    sales_default_location: SystemLocationReferenceModel | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    restrict_default_warehouse_flag: bool | None
    restrict_default_warehouse_bin_flag: bool | None
    sso_session_flag: bool | None
    sso_client_id: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True