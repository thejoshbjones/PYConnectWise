from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
class Category(str, Enum):
    Reactive = 'Reactive'
    Proactive = 'Proactive'

class BoardTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    category: Category | None
    default_flag: bool | None
    inactive_flag: bool | None
    request_for_change_flag: bool | None
    integration_xref: str | None
    board: BoardReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True