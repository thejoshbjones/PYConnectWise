from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class AccountingBatchModel(ConnectWiseModel):
    id: int | None
    batch_identifier: str | None
    export_invoices_flag: bool | None
    export_expenses_flag: bool | None
    export_products_flag: bool | None
    closed_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True