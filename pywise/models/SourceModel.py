from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class SourceModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    _info: dict[str, str] | None
    entered_by: str | None
    date_entered: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True