from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel

class PaymentModel(ConnectWiseModel):
    id: int
    type: str
    invoice: InvoiceReferenceModel
    credit: InvoiceReferenceModel
    amount: float
    payment_date: str
    applied_by: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True