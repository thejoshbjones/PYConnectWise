from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.SLAReferenceModel import SLAReferenceModel

class SLAPriorityModel(ConnectWiseModel):
    id: int | None
    priority: PriorityReferenceModel | None
    respond_hours: float | None
    respond_percent: int | None
    plan_within: float | None
    plan_within_percent: int | None
    resolution_hours: float | None
    resolution_percent: int | None
    sla: SLAReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True