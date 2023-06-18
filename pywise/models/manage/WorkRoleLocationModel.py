from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class WorkRoleLocationModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    hourly_rate: float | None
    work_role: WorkRoleReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True