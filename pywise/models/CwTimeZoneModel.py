from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CwTimeZoneModel(ConnectWiseModel):
    id: int | None
    name: str | None
    offset: float | None
    start_date: str | None
    end_date: str | None
    daylight_savings_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True