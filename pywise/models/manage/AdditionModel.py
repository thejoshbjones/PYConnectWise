from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from enum import Enum
from pywise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.manage.InvoiceGroupingReferenceModel import InvoiceGroupingReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class BillCustomer(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
class AgreementStatus(str, Enum):
    Active = 'Active'
    Cancelled = 'Cancelled'
    Expired = 'Expired'
    Inactive = 'Inactive'

class AdditionModel(ConnectWiseModel):
    id: int | None
    product: IvItemReferenceModel | None
    quantity: float | None
    less_included: float | None
    unit_price: float | None
    unit_cost: float | None
    bill_customer: BillCustomer | None
    effective_date: str | None
    cancelled_date: str | None
    taxable_flag: bool | None
    serial_number: str | None
    invoice_description: str | None
    purchase_item_flag: bool | None
    special_order_flag: bool | None
    agreement_id: int | None
    description: str | None
    billed_quantity: float | None
    uom: str | None
    ext_price: float | None
    ext_cost: float | None
    sequence_number: float | None
    margin: float | None
    prorate_cost: float | None
    prorate_price: float | None
    extended_prorate_cost: float | None
    extended_prorate_price: float | None
    prorate_current_period_flag: bool | None
    opportunity: OpportunityReferenceModel | None
    agreement_status: AgreementStatus | None
    invoice_grouping: InvoiceGroupingReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True