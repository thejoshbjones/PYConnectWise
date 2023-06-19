from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.GLExportAdjustmentTransactionDetailModel import GLExportAdjustmentTransactionDetailModel

class GLExportAdjustmentTransactionModel(ConnectWiseModel):
    id: str
    document_type: str
    document_date: str
    gl_type_i_d: str
    account_number: str
    memo: str
    gl_class: str
    adjustment_description: str
    adjustment_detail: list[GLExportAdjustmentTransactionDetailModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True