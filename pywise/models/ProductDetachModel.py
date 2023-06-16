from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class ProductDetachModel(ConnectWiseModel):
    remove_from_ticket: bool | None
    remove_from_invoice: bool | None
    remove_from_opportunity: bool | None
    remove_from_sales_order: bool | None
    remove_from_project: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True