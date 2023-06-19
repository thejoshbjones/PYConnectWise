from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ExpenseTaxTypeReferenceModel import ExpenseTaxTypeReferenceModel

class ExpenseTaxModel(ConnectWiseModel):
    id: int
    amount: float
    type: ExpenseTaxTypeReferenceModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True