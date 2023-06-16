from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class InvoiceGroupingReferenceModel(ConnectWiseModel):
    id: int | None
    name: str | None
    description: str | None
    show_price_flag: bool | None
    show_sub_items_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True