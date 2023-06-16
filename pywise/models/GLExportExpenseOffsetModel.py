from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class GLExportExpenseOffsetModel(ConnectWiseModel):
    id: int | None
    document_date: str | None
    document_type: str | None
    account_number: str | None
    gl_type_id: str | None
    gl_class: str | None
    member: MemberReferenceModel | None
    memo: str | None
    description: str | None
    total: float | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True