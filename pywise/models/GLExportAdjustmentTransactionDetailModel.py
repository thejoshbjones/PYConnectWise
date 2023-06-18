from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.IvItemReferenceModel import IvItemReferenceModel

class GLExportAdjustmentTransactionDetailModel(ConnectWiseModel):
    gl_class: str | None
    description: str | None
    memo: str | None
    item: IvItemReferenceModel | None
    quantity: int | None
    total: float | None
    cost: float | None
    cost_account_number: str | None
    inventory_account_number: str | None
    account_number: str | None
    product_account_number: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True