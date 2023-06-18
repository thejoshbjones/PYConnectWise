from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CountryInfoModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    city_caption: str | None
    state_caption: str | None
    zip_caption: str | None
    dialing_prefix: str | None
    localization_caption_one: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True