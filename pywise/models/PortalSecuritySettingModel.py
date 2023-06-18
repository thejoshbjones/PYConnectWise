from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class PortalSecuritySettingModel(ConnectWiseModel):
    id: int | None
    function_identifier: str | None
    function_description: str | None
    level_one: bool | None
    level_two: bool | None
    level_three: bool | None
    level_four: bool | None
    level_five: bool | None
    level_six: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True