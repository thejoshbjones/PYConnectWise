from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel

class StandardNoteInfoModel(ConnectWiseModel):
    id: int | None
    name: str | None
    contents: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    board: BoardReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True