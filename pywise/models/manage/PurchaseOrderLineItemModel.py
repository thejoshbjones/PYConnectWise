from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from enum import Enum
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class ReceivedStatus(str, Enum):
    Waiting = 'Waiting'
    FullyReceived = 'FullyReceived'
    PartiallyReceiveCancelRest = 'PartiallyReceiveCancelRest'
    PartiallyReceiveCloneRest = 'PartiallyReceiveCloneRest'

class PurchaseOrderLineItemModel(ConnectWiseModel):
    id: int | None
    backordered_flag: bool | None
    canceled_by: str | None
    canceled_flag: bool | None
    canceled_reason: str | None
    closed_flag: bool | None
    date_canceled: str | None
    date_canceled_utc: str | None
    description: str | None
    display_internal_notes_flag: bool | None
    expected_ship_date: str | None
    internal_notes: str | None
    line_number: int | None
    packing_slip: str | None
    product: IvItemReferenceModel | None
    purchase_order_id: int | None
    quantity: float | None
    received_quantity: int | None
    serial_numbers: str | None
    ship_date: str | None
    shipment_method: ShipmentMethodReferenceModel | None
    tax: float | None
    tracking_number: str | None
    unit_cost: float | None
    unit_of_measure: UnitOfMeasureReferenceModel | None
    vendor_order_number: str | None
    vendor_sku: str | None
    warehouse: WarehouseReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    ship_set: str | None
    date_received: str | None
    received_status: ReceivedStatus | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True