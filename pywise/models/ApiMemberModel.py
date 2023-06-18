from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.SecurityRoleReferenceModel import SecurityRoleReferenceModel
from pywise.models.StructureReferenceModel import StructureReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel

class ApiMemberModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    name: str | None
    email_address: str | None
    inactive_flag: bool | None
    inactive_date: str | None
    time_zone: TimeZoneSetupReferenceModel | None
    security_role: SecurityRoleReferenceModel | None
    structure_level: StructureReferenceModel | None
    security_location: SystemLocationReferenceModel | None
    default_location: SystemLocationReferenceModel | None
    default_department: SystemDepartmentReferenceModel | None
    sales_default_location: SystemLocationReferenceModel | None
    service_default_board: BoardReferenceModel | None
    notes: str | None
    excluded_service_board_ids: list[int] | None
    block_price_flag: bool | None
    block_cost_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True