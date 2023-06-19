from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.OnHandSerialNumberReferenceModel import OnHandSerialNumberReferenceModel

class InventoryOnHandModel(ConnectWiseModel):
    id: int
    catalog_item: CatalogItemReferenceModel
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    on_hand: int
    serial_numbers: list[OnHandSerialNumberReferenceModel]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True