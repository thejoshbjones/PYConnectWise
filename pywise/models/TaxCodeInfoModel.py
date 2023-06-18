from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class TaxCodeInfoModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    description: str | None
    effective_date: str | None
    cancel_date: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True