from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class BillingStatusModel(ConnectWiseModel):
    id: int | None
    name: str | None
    sort_order: int | None
    default_flag: bool | None
    closed_flag: bool | None
    inactive_flag: bool | None
    sent_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True