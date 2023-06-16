from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.OnHandSerialNumberReferenceModel import OnHandSerialNumberReferenceModel

class CatalogInventoryModel(ConnectWiseModel):
    id: int | None
    catalog_item: CatalogItemReferenceModel | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    on_hand: int | None
    serial_numbers: list[OnHandSerialNumberReferenceModel] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True