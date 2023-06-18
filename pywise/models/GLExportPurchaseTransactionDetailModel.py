from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel

class GLExportPurchaseTransactionDetailModel(ConnectWiseModel):
    id: int | None
    document_date: str | None
    gl_class: str | None
    gl_type_id: str | None
    gl_item_id: str | None
    sales_code: str | None
    description: str | None
    cost: float | None
    memo: str | None
    tax_note: str | None
    vendor_number: str | None
    account_number: str | None
    cost_account_number: str | None
    inventory_account_number: str | None
    vendor_account_number: str | None
    item: IvItemReferenceModel | None
    item_description: str | None
    sales_description: str | None
    taxable: bool | None
    item_price: float | None
    item_cost: float | None
    unit_of_measure: UnitOfMeasureReferenceModel | None
    quantity: float | None
    total: float | None
    currency: CurrencyReferenceModel | None
    serialized_flag: bool | None
    serial_numbers: str | None
    drop_shipped_flag: bool | None
    line_number: int | None
    warehouse_bin: WarehouseBinReferenceModel | None
    warehouse_site: SiteReferenceModel | None
    sub_category: ProductSubCategoryReferenceModel | None
    shipment_method: ShipmentMethodReferenceModel | None
    item_type_xref: str | None
    inventory_xref: str | None
    cogs_xref: str | None
    uom_schedule_xref: str | None
    price_level_xref: str | None
    location_xref: str | None
    tax_code: TaxCodeReferenceModel | None
    purchase_header_tax_group: str | None
    tax_code_xref: str | None
    tax_rate: float | None
    tax_agency_xref: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True