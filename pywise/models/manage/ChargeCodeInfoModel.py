from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class ChargeCodeInfoModel(ConnectWiseModel):
    id: int
    name: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    expense_entry_flag: bool
    allow_all_expense_type_flag: bool
    time_entry_flag: bool
    work_type: WorkTypeReferenceModel
    work_role: WorkRoleReferenceModel
    expense_type_ids: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True