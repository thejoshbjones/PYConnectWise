from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel

class ExpenseTypeExemptionModel(ConnectWiseModel):
    id: int | None
    expense_type: ExpenseTypeReferenceModel | None
    taxable_levels: list[int] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True