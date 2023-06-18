from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class BillingOptions(str, Enum):
    BiMonthly = 'BiMonthly'
    BiWeekly = 'BiWeekly'
    Monthly = 'Monthly'
    NotRecurring = 'NotRecurring'
    Quarterly = 'Quarterly'
    SemiAnnual = 'SemiAnnual'
    Weekly = 'Weekly'
    Yearly = 'Yearly'

class BillingCycleModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    name: str | None
    default_flag: bool | None
    billing_options: BillingOptions | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True