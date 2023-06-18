from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.manage.PurchaseOrderReferenceModel import PurchaseOrderReferenceModel
from pywise.models.manage.PurchaseOrderLineItemReferenceModel import PurchaseOrderLineItemReferenceModel
from pywise.models.manage.ExpenseDetailReferenceModel import ExpenseDetailReferenceModel
from pywise.models.manage.AdjustmentDetailReferenceModel import AdjustmentDetailReferenceModel

class BatchEntryModel(ConnectWiseModel):
    id: int | None
    account_type: str | None
    name: str | None
    account_number: str | None
    debit: float | None
    credit: float | None
    cost: float | None
    item: str | None
    sales_code: str | None
    cost_of_goods_sold_account_number: str | None
    invoice: InvoiceReferenceModel | None
    purchase_order: PurchaseOrderReferenceModel | None
    line_item: PurchaseOrderLineItemReferenceModel | None
    transfer: str | None
    expense: ExpenseDetailReferenceModel | None
    adjustment_detail: AdjustmentDetailReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True