from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class UsageModel(ConnectWiseModel):
    type: str | None
    count: int | None
    id: int | None
    description: str | None
    hyperlink: str | None
    type_key: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True