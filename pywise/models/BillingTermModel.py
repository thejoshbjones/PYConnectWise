from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class BillingTermModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    due_days: int | None
    terms_xref: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True