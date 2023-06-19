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
    id: int
    document_date: str
    account_number: str
    gl_class: str
    cost: float
    sales_code: str
    gl_type_id: str
    gl_item_id: str
    memo: str
    vendor_number: str
    vendor_account_number: str
    cost_account_number: str
    inventory_account_number: str
    item_type_xref: str
    inventory_xref: str
    cogs_xref: str
    uom_schedule_xref: str
    price_level_xref: str
    location_xref: str
    item: IvItemReferenceModel
    taxable_flag: bool
    sales_description: str
    item_description: str
    item_price: float
    item_cost: float
    unit_of_measure: UnitOfMeasureReferenceModel
    quantity: float
    total: float
    currency: CurrencyReferenceModel
    serialized_flag: bool
    serial_numbers: str
    drop_shipped_flag: bool
    line_number: int
    warehouse_site: SiteReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    shipment_method: ShipmentMethodReferenceModel
    sub_category: ProductSubCategoryReferenceModel
    tax_code: TaxCodeReferenceModel
    tax_rate: float
    tax_rate_percent: float
    tax_agency_xref: str
    tax_note: str
    purchase_header_tax_group: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True