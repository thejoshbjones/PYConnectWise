from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.manage.ProductTypeReferenceModel import ProductTypeReferenceModel
from enum import Enum
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.ManufacturerReferenceModel import ManufacturerReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SLAReferenceModel import SLAReferenceModel
from pywise.models.manage.EntityTypeReferenceModel import EntityTypeReferenceModel
from pywise.models.manage.BillingCycleReferenceModel import BillingCycleReferenceModel
from pywise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class ProductClass(str, Enum):
    Agreement = 'Agreement'
    Bundle = 'Bundle'
    Inventory = 'Inventory'
    NonInventory = 'NonInventory'
    Service = 'Service'
class PriceAttribute(str, Enum):
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
    TimeAndMaterials = 'TimeAndMaterials'
class RecurringCycleType(str, Enum):
    ContractYear = 'ContractYear'
    CalendarYear = 'CalendarYear'

class CatalogItemModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    description: str | None
    inactive_flag: bool | None
    subcategory: ProductSubCategoryReferenceModel | None
    type: ProductTypeReferenceModel | None
    product_class: ProductClass | None
    serialized_flag: bool | None
    serialized_cost_flag: bool | None
    phase_product_flag: bool | None
    unit_of_measure: UnitOfMeasureReferenceModel | None
    min_stock_level: int | None
    price: float | None
    cost: float | None
    price_attribute: PriceAttribute | None
    taxable_flag: bool | None
    drop_ship_flag: bool | None
    special_order_flag: bool | None
    customer_description: str | None
    manufacturer: ManufacturerReferenceModel | None
    manufacturer_part_number: str | None
    vendor: CompanyReferenceModel | None
    vendor_sku: str | None
    notes: str | None
    integration_x_ref: str | None
    sla: SLAReferenceModel | None
    entity_type: EntityTypeReferenceModel | None
    recurring_flag: bool | None
    recurring_revenue: float | None
    recurring_cost: float | None
    recurring_one_time_flag: bool | None
    recurring_bill_cycle: BillingCycleReferenceModel | None
    recurring_cycle_type: RecurringCycleType | None
    date_entered: str | None
    calculated_price_flag: bool | None
    calculated_cost_flag: bool | None
    category: ProductCategoryReferenceModel | None
    calculated_price: float | None
    calculated_cost: float | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True