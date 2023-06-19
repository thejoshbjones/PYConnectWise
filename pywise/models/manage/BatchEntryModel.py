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
    id: int
    account_type: str
    name: str
    account_number: str
    debit: float
    credit: float
    cost: float
    item: str
    sales_code: str
    cost_of_goods_sold_account_number: str
    invoice: InvoiceReferenceModel
    purchase_order: PurchaseOrderReferenceModel
    line_item: PurchaseOrderLineItemReferenceModel
    transfer: str
    expense: ExpenseDetailReferenceModel
    adjustment_detail: AdjustmentDetailReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True