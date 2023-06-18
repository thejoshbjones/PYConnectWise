from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.GLExportInventoryTransferOffsetModel import GLExportInventoryTransferOffsetModel

class GLExportInventoryTransferModel(ConnectWiseModel):
    id: str | None
    document_type: str | None
    document_date: str | None
    account_number: str | None
    gl_class: str | None
    gl_type_id: str | None
    description: str | None
    sales_code: str | None
    memo: str | None
    cost_account_number: str | None
    inventory_account_number: str | None
    transfer_id: int | None
    item: IvItemReferenceModel | None
    gl_item_id: str | None
    sales_description: str | None
    item_description: str | None
    currency: CurrencyReferenceModel | None
    item_price: float | None
    taxable: bool | None
    unit_of_measure: UnitOfMeasureReferenceModel | None
    quantity: float | None
    cost: float | None
    total: float | None
    sub_category: ProductSubCategoryReferenceModel | None
    serialized_flag: bool | None
    serial_numbers: str | None
    bin: WarehouseBinReferenceModel | None
    warehouse: WarehouseReferenceModel | None
    transfer_from_bin: WarehouseBinReferenceModel | None
    transfer_from_location_xref: str | None
    transfer_to_bin: WarehouseBinReferenceModel | None
    transfer_to_location_xref: str | None
    location_xref: str | None
    price_level_xref: str | None
    uom_schedule_xref: str | None
    item_type_xref: str | None
    inventory_xref: str | None
    cogs_xref: str | None
    tax_note: str | None
    offset: GLExportInventoryTransferOffsetModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True