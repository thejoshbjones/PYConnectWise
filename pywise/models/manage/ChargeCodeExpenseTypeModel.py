from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel
from pywise.models.manage.ChargeCodeReferenceModel import ChargeCodeReferenceModel

class ChargeCodeExpenseTypeModel(ConnectWiseModel):
    id: int | None
    type: ExpenseTypeReferenceModel | None
    charge_code: ChargeCodeReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True