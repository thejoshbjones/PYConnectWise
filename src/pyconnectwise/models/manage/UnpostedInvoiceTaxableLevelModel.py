from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class UnpostedInvoiceTaxableLevelModel(ConnectWiseModel):
    id: int
    tax_level: int
    tax_code_xref: str
    tax_amount: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True