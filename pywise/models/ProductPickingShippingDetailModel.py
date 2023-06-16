from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.ProductItemReferenceModel import ProductItemReferenceModel

class ProductPickingShippingDetailModel(ConnectWiseModel):
    id: int | None
    picked_quantity: int | None
    shipped_quantity: int | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    shipment_method: ShipmentMethodReferenceModel | None
    serial_number: str | None
    serial_number_ids: list[int] | None
    tracking_number: str | None
    product_item: ProductItemReferenceModel | None
    line_number: int | None
    quantity: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True