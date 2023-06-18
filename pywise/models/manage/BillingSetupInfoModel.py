from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class BillingSetupInfoModel(ConnectWiseModel):
    id: int | None
    remit_name: str | None
    location: SystemLocationReferenceModel | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True