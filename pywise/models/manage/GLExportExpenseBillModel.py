from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.GLExportExpenseBillDetailModel import GLExportExpenseBillDetailModel

class GLExportExpenseBillModel(ConnectWiseModel):
    id: int | None
    document_date: str | None
    document_type: str | None
    document_number: str | None
    memo: str | None
    gl_class: str | None
    ap_account_number: str | None
    member: MemberReferenceModel | None
    vendor_number: str | None
    currency: CurrencyReferenceModel | None
    total: float | None
    detail: list[GLExportExpenseBillDetailModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True