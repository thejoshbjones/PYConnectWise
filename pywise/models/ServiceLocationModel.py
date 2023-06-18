from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Where(str, Enum):
    OnSite = 'OnSite'
    Remote = 'Remote'
    InHouse = 'InHouse'

class ServiceLocationModel(ConnectWiseModel):
    id: int | None
    name: str | None
    where: Where | None
    default_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True