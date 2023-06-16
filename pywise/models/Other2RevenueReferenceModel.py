from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class Other2RevenueReferenceModel(ConnectWiseModel):
    id: int | None
    revenue: float | None
    cost: float | None
    margin: float | None
    percentage: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True