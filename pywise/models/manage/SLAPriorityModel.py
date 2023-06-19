from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.SLAReferenceModel import SLAReferenceModel

class SLAPriorityModel(ConnectWiseModel):
    id: int
    priority: PriorityReferenceModel
    respond_hours: float
    respond_percent: int
    plan_within: float
    plan_within_percent: int
    resolution_hours: float
    resolution_percent: int
    sla: SLAReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True