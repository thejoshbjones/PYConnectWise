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
    id: int | None
    catalog_item: CatalogItemReferenceModel | None
    description: str | None
    quantity_on_hand: float | None
    unit_cost: float | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    quantity_adjusted: int | None
    serial_number: str | None
    adjustment: AdjustmentReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True