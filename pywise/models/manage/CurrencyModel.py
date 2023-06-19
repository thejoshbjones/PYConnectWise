from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CurrencyCodeReferenceModel import CurrencyCodeReferenceModel

class CurrencyModel(ConnectWiseModel):
    id: int
    currency_identifier: str
    name: str
    symbol: str
    display_id_flag: bool
    display_symbol_flag: bool
    currency_code: CurrencyCodeReferenceModel
    thousands_separator: str
    decimal_separator: str
    negative_parentheses_flag: bool
    right_align: bool
    number_of_decimals: int
    report_format: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True