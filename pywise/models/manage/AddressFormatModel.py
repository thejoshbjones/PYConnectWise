from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class AddressFormatModel(ConnectWiseModel):
    id: int | None
    name: str | None
    format: str | None
    default_flag: bool | None
    country_ids: list[int] | None
    add_all_countries: bool | None
    remove_all_countries: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True