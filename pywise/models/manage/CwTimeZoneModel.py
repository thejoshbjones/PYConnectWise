from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CwTimeZoneModel(ConnectWiseModel):
    id: int
    name: str
    offset: float
    start_date: str
    end_date: str
    daylight_savings_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True