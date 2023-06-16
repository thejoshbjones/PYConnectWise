from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CatalogItemReferenceModel import CatalogItemReferenceModel
from enum import Enum
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ProductRecurringModel import ProductRecurringModel
from pywise.models.SLAReferenceModel import SLAReferenceModel
from pywise.models.EntityTypeReferenceModel import EntityTypeReferenceModel
from pywise.models.TicketReferenceModel import TicketReferenceModel
from pywise.models.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.SalesOrderReferenceModel import SalesOrderReferenceModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.InvoiceGroupingReferenceModel import InvoiceGroupingReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel
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
    id: int | None
    catalog_item: CatalogItemReferenceModel | None
    description: str | None
    sequence_number: float | None
    quantity: float | None
    price: float | None
    cost: float | None
    discount: float | None
    agreement_amount: float | None
    price_method: PriceMethod | None
    billable_option: BillableOption | None
    agreement: AgreementReferenceModel | None
    location_id: int | None
    business_unit_id: int | None
    vendor: CompanyReferenceModel | None
    vendor_sku: str | None
    taxable_flag: bool | None
    dropship_flag: bool | None
    special_order_flag: bool | None
    phase_product_flag: bool | None
    cancelled_flag: bool | None
    quantity_cancelled: float | None
    cancelled_reason: str | None
    customer_description: str | None
    internal_notes: str | None
    product_supplied_flag: bool | None
    sub_contractor_ship_to_id: int | None
    sub_contractor_amount_limit: float | None
    recurring: ProductRecurringModel | None
    sla: SLAReferenceModel | None
    entity_type: EntityTypeReferenceModel | None
    ticket: TicketReferenceModel | None
    project: ProjectReferenceModel | None
    phase: ProjectPhaseReferenceModel | None
    sales_order: SalesOrderReferenceModel | None
    opportunity: OpportunityReferenceModel | None
    invoice: InvoiceReferenceModel | None
    warehouse_id: int | None
    warehouse_bin_id: int | None
    calculated_price_flag: bool | None
    calculated_cost_flag: bool | None
    forecast_detail_id: int | None
    cancelled_by: int | None
    cancelled_date: str | None
    warehouse: str | None
    warehouse_bin: str | None
    purchase_date: str | None
    integration_x_ref: str | None
    list_price: float | None
    serial_number_ids: list[int] | None
    company: CompanyReferenceModel | None
    forecast_status: OpportunityStatusReferenceModel | None
    product_class: ProductClass | None
    need_to_purchase_flag: bool | None
    need_to_order_quantity: int | None
    minimum_stock_flag: bool | None
    ship_set: str | None
    calculated_price: float | None
    calculated_cost: float | None
    invoice_grouping: InvoiceGroupingReferenceModel | None
    po_approved_flag: bool | None
    add_components_flag: bool | None
    ignore_pricing_schedules_flag: bool | None
    _info: dict[str, str] | None
    bypass_forecast_update: bool | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True