from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CategoryModel(ConnectWiseModel):
    id: int | None
    name: str | None
    inactive_flag: bool | None
    price_level_xref: str | None
    integration_xref: str | None
    location_ids: list[int] | None
    default_flag: bool | None
    add_all_locations: bool | None
    remove_all_locations: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True