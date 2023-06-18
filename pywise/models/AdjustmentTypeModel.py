from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class AdjustmentTypeModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    name: str | None
    audit_trail_flag: bool | None
    date_created: str | None
    created_by: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True