from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel

class GLExportPurchaseTransactionDetailTaxModel(ConnectWiseModel):
    id: int | None
    document_date: str | None
    account_number: str | None
    gl_class: str | None
    cost: float | None
    sales_code: str | None
    gl_type_id: str | None
    gl_item_id: str | None
    memo: str | None
    vendor_number: str | None
    vendor_account_number: str | None
    cost_account_number: str | None
    inventory_account_number: str | None
    item_type_xref: str | None
    inventory_xref: str | None
    cogs_xref: str | None
    uom_schedule_xref: str | None
    price_level_xref: str | None
    location_xref: str | None
    item: IvItemReferenceModel | None
    taxable_flag: bool | None
    sales_description: str | None
    item_description: str | None
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
    warehouse_site: SiteReferenceModel | None
    warehouse_bin: WarehouseBinReferenceModel | None
    shipment_method: ShipmentMethodReferenceModel | None
    sub_category: ProductSubCategoryReferenceModel | None
    tax_code: TaxCodeReferenceModel | None
    tax_rate: float | None
    tax_rate_percent: float | None
    tax_agency_xref: str | None
    tax_note: str | None
    purchase_header_tax_group: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True