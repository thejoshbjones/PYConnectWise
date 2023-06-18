from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class PrefixSuffixType(str, Enum):
    Prefix = 'Prefix'
    Suffix = 'Suffix'
class CostingMethod(str, Enum):
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    AverageCosting = 'AverageCosting'

class ProcurementSettingModel(ConnectWiseModel):
    id: int | None
    starting_purchase_order_num: int | None
    purchase_order_prefix: str | None
    purchase_order_suffix: str | None
    prefix_suffix_type: PrefixSuffixType | None
    disable_cost_updates_flag: bool | None
    disable_negative_inventory_flag: bool | None
    costing_method: CostingMethod | None
    auto_close_purchase_order_flag: bool | None
    auto_close_purchase_order_item_flag: bool | None
    auto_approve_purchase_order_flag: bool | None
    tax_purchase_order_flag: bool | None
    tax_freight_flag: bool | None
    use_vendor_tax_code_flag: bool | None
    num_decimal_places: int | None
    disable_auto_pick_flag: bool | None
    default_product_taxable_flag: bool | None
    eori_number: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True