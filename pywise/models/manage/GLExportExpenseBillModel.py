from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.GLExportExpenseBillDetailModel import GLExportExpenseBillDetailModel

class GLExportExpenseBillModel(ConnectWiseModel):
    id: int
    document_date: str
    document_type: str
    document_number: str
    memo: str
    gl_class: str
    ap_account_number: str
    member: MemberReferenceModel
    vendor_number: str
    currency: CurrencyReferenceModel
    total: float
    detail: list[GLExportExpenseBillDetailModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True