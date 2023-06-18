from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.GLExportAdjustmentTransactionDetailModel import GLExportAdjustmentTransactionDetailModel

class GLExportAdjustmentTransactionModel(ConnectWiseModel):
    id: str | None
    document_type: str | None
    document_date: str | None
    gl_type_i_d: str | None
    account_number: str | None
    memo: str | None
    gl_class: str | None
    adjustment_description: str | None
    adjustment_detail: list[GLExportAdjustmentTransactionDetailModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True