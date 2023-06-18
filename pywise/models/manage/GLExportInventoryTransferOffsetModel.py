from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class GLExportInventoryTransferOffsetModel(ConnectWiseModel):
    id: int | None
    document_type: str | None
    document_date: str | None
    account_number: str | None
    gl_class: str | None
    total: float | None
    memo: str | None
    description: str | None
    gl_type_id: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True