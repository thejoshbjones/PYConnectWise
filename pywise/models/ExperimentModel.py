from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class ExperimentModel(ConnectWiseModel):
    id: int | None
    experiment_id: str | None
    name: str | None
    description: str | None
    properties: str | None
    inactive_flag: bool | None
    member_inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True