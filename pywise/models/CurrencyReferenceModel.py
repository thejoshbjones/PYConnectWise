from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CurrencyReferenceModel(ConnectWiseModel):
    id: int | None
    symbol: str | None
    currency_code: str | None
    decimal_separator: str | None
    number_of_decimals: int | None
    thousands_separator: str | None
    negative_parentheses_flag: bool | None
    display_symbol_flag: bool | None
    currency_identifier: str | None
    display_id_flag: bool | None
    right_align: bool | None
    name: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True