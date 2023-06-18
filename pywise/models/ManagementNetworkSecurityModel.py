from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class ManagementNetworkSecurityModel(ConnectWiseModel):
    id: int | None
    name: str | None
    username: str | None
    password: str | None
    site: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True