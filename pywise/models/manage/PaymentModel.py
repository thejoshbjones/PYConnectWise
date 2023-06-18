from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel

class PaymentModel(ConnectWiseModel):
    id: int | None
    type: str | None
    invoice: InvoiceReferenceModel | None
    credit: InvoiceReferenceModel | None
    amount: float | None
    payment_date: str | None
    applied_by: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True