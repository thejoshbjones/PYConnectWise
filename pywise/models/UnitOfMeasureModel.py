from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class UnitOfMeasureModel(ConnectWiseModel):
    id: int | None
    name: str | None
    inactive_flag: bool | None
    default_flag: bool | None
    uom_schedule_xref: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True