from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ProductClass(str, Enum):
    Agreement = 'Agreement'
    Bundle = 'Bundle'
    Inventory = 'Inventory'
    NonInventory = 'NonInventory'
    Service = 'Service'

class CatalogItemInfoModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    description: str | None
    inactive_flag: bool | None
    product_class: ProductClass | None
    serialized_cost_flag: bool | None
    price: float | None
    cost: float | None
    taxable_flag: bool | None
    drop_ship_flag: bool | None
    special_order_flag: bool | None
    customer_description: str | None
    manufacturer_part_number: str | None
    vendor_sku: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True