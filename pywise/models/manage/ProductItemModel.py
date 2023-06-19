from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from enum import Enum
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ProductRecurringModel import ProductRecurringModel
from pywise.models.manage.SLAReferenceModel import SLAReferenceModel
from pywise.models.manage.EntityTypeReferenceModel import EntityTypeReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.manage.SalesOrderReferenceModel import SalesOrderReferenceModel
from pywise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.manage.InvoiceGroupingReferenceModel import InvoiceGroupingReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class PriceMethod(str, Enum):
    FlatRateForRange = 'FlatRateForRange'
    PercentMarkupFromCost = 'PercentMarkupFromCost'
    PercentMarkdownFromPrice = 'PercentMarkdownFromPrice'
    PricePerUnit = 'PricePerUnit'
class BillableOption(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
class ProductClass(str, Enum):
    Agreement = 'Agreement'
    Bundle = 'Bundle'
    Inventory = 'Inventory'
    NonInventory = 'NonInventory'
    Service = 'Service'

class ProductItemModel(ConnectWiseModel):
    id: int
    catalog_item: CatalogItemReferenceModel
    description: str
    sequence_number: float
    quantity: float
    price: float
    cost: float
    discount: float
    agreement_amount: float
    price_method: PriceMethod
    billable_option: BillableOption
    agreement: AgreementReferenceModel
    location_id: int
    business_unit_id: int
    vendor: CompanyReferenceModel
    vendor_sku: str
    taxable_flag: bool
    dropship_flag: bool
    special_order_flag: bool
    phase_product_flag: bool
    cancelled_flag: bool
    quantity_cancelled: float
    cancelled_reason: str
    customer_description: str
    internal_notes: str
    product_supplied_flag: bool
    sub_contractor_ship_to_id: int
    sub_contractor_amount_limit: float
    recurring: ProductRecurringModel
    sla: SLAReferenceModel
    entity_type: EntityTypeReferenceModel
    ticket: TicketReferenceModel
    project: ProjectReferenceModel
    phase: ProjectPhaseReferenceModel
    sales_order: SalesOrderReferenceModel
    opportunity: OpportunityReferenceModel
    invoice: InvoiceReferenceModel
    warehouse_id: int
    warehouse_bin_id: int
    calculated_price_flag: bool
    calculated_cost_flag: bool
    forecast_detail_id: int
    cancelled_by: int
    cancelled_date: str
    warehouse: str
    warehouse_bin: str
    purchase_date: str
    integration_x_ref: str
    list_price: float
    serial_number_ids: list[int]
    company: CompanyReferenceModel
    forecast_status: OpportunityStatusReferenceModel
    product_class: ProductClass
    need_to_purchase_flag: bool
    need_to_order_quantity: int
    minimum_stock_flag: bool
    ship_set: str
    calculated_price: float
    calculated_cost: float
    invoice_grouping: InvoiceGroupingReferenceModel
    po_approved_flag: bool
    add_components_flag: bool
    ignore_pricing_schedules_flag: bool
    _info: dict[str, str]
    bypass_forecast_update: bool
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True