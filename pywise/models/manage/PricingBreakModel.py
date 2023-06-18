from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class PriceMethod(str, Enum):
    FlatRateForRange = 'FlatRateForRange'
    PercentMarkupFromCost = 'PercentMarkupFromCost'
    PercentMarkdownFromPrice = 'PercentMarkdownFromPrice'
    PricePerUnit = 'PricePerUnit'

class PricingBreakModel(ConnectWiseModel):
    id: int | None
    detail_id: int | None
    amount: float | None
    quantity_start: float | None
    quantity_end: float | None
    unlimited: bool | None
    price_method: PriceMethod | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True