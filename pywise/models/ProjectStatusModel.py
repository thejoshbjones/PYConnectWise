from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.StatusIndicatorReferenceModel import StatusIndicatorReferenceModel

class ProjectStatusModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    inactive_flag: bool | None
    no_time_flag: bool | None
    closed_flag: bool | None
    status_indicator: StatusIndicatorReferenceModel | None
    custom_status_indicator_name: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True