from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class RateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'

class TaxCodeLevelModel(ConnectWiseModel):
    id: int | None
    tax_level: int | None
    tax_rate: float | None
    rate_type: RateType | None
    taxable_max: float | None
    caption: str | None
    tax_code_xref: str | None
    agency_xref: str | None
    tax_services_flag: bool | None
    tax_expenses_flag: bool | None
    tax_products_flag: bool | None
    single_unit_flag: bool | None
    single_unit_minimum: float | None
    single_unit_maximum: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True