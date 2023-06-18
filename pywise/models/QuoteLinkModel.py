from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel

class QuoteLinkModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    link: str | None
    all_locations_flag: bool | None
    new_window_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True