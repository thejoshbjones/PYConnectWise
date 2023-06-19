from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.AdjustmentReferenceModel import AdjustmentReferenceModel

class AdjustmentDetailModel(ConnectWiseModel):
    id: int
    catalog_item: CatalogItemReferenceModel
    description: str
    quantity_on_hand: float
    unit_cost: float
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    quantity_adjusted: int
    serial_number: str
    adjustment: AdjustmentReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True