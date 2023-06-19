from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.TimeEntryReferenceModel import TimeEntryReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.ProductReferenceModel import ProductReferenceModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.manage.GLExportTransactionDetailTaxLevelModel import GLExportTransactionDetailTaxLevelModel

class GLExportTransactionDetailModel(ConnectWiseModel):
    id: int
    document_date: str
    document_type: str
    account_number: str
    gl_class: str
    gl_type_id: str
    gl_item_id: str
    invoice_summary_option: str
    cost: float
    sales_code: str
    memo: str
    description: str
    quantity: float
    total: float
    currency: CurrencyReferenceModel
    time_entry: TimeEntryReferenceModel
    cost_account_number: str
    inventory_account_number: str
    product_account_number: str
    tax_code: TaxCodeReferenceModel
    tax_code_xref: str
    tax_agency_xref: str
    tax_note: str
    tax_rate: float
    tax_rate_percent: float
    taxable_flag: bool
    taxable2_flag: bool
    taxable3_flag: bool
    taxable4_flag: bool
    taxable5_flag: bool
    item: IvItemReferenceModel
    product: ProductReferenceModel
    item_taxable_flag: bool
    item_price: float
    item_cost: float
    item_description: str
    sales_description: str
    unit_of_measure: UnitOfMeasureReferenceModel
    sub_category: ProductSubCategoryReferenceModel
    serialized_flag: bool
    serial_numbers: str
    warehouse_site: SiteReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    shipment_method: ShipmentMethodReferenceModel
    drop_shipped_flag: bool
    item_type_xref: str
    inventory_xref: str
    cogs_xref: str
    uom_schedule_xref: str
    price_level_xref: str
    location_xref: str
    tax_levels: list[GLExportTransactionDetailTaxLevelModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True