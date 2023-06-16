from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class SetupScreenModel(ConnectWiseModel):
    id: int | None
    category: str | None
    name: str | None
    description: str | None
    module_description: str | None
    module_identifier: str | None
    module_name: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True