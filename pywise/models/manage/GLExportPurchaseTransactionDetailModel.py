from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel

class GLExportPurchaseTransactionDetailModel(ConnectWiseModel):
    id: int
    document_date: str
    gl_class: str
    gl_type_id: str
    gl_item_id: str
    sales_code: str
    description: str
    cost: float
    memo: str
    tax_note: str
    vendor_number: str
    account_number: str
    cost_account_number: str
    inventory_account_number: str
    vendor_account_number: str
    item: IvItemReferenceModel
    item_description: str
    sales_description: str
    taxable: bool
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
    warehouse_bin: WarehouseBinReferenceModel
    warehouse_site: SiteReferenceModel
    sub_category: ProductSubCategoryReferenceModel
    shipment_method: ShipmentMethodReferenceModel
    item_type_xref: str
    inventory_xref: str
    cogs_xref: str
    uom_schedule_xref: str
    price_level_xref: str
    location_xref: str
    tax_code: TaxCodeReferenceModel
    purchase_header_tax_group: str
    tax_code_xref: str
    tax_rate: float
    tax_agency_xref: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True