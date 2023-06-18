from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.IvItemReferenceModel import IvItemReferenceModel
from enum import Enum
from pywise.models.BillingCycleReferenceModel import BillingCycleReferenceModel
class ForecastType(str, Enum):
    Other1 = 'Other1'
    Other2 = 'Other2'
    Agreement = 'Agreement'
    Product = 'Product'
    Service = 'Service'

class ForecastItemModel(ConnectWiseModel):
    id: int | None
    forecast_description: str | None
    opportunity: OpportunityReferenceModel | None
    quantity: float | None
    status: OpportunityStatusReferenceModel | None
    catalog_item: IvItemReferenceModel | None
    product_description: str | None
    product_class: str | None
    revenue: float | None
    cost: float | None
    margin: float | None
    percentage: int | None
    include_flag: bool | None
    quote_werks_doc_no: str | None
    quote_werks_doc_name: str | None
    quote_werks_quantity: int | None
    forecast_type: ForecastType | None
    link_flag: bool | None
    recurring_revenue: float | None
    recurring_cost: float | None
    recurring_date_start: str | None
    recurring_date_end: str | None
    bill_cycle: BillingCycleReferenceModel | None
    cycle_basis: str | None
    cycles: int | None
    recurring_flag: bool | None
    sequence_number: float | None
    sub_number: int | None
    taxable_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True