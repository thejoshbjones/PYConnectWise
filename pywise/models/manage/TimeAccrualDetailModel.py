from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.TimeAccrualReferenceModel import TimeAccrualReferenceModel
class AccrualType(str, Enum):
    Holiday = 'Holiday'
    PTO = 'PTO'
    Sick = 'Sick'
    Vacation = 'Vacation'

class TimeAccrualDetailModel(ConnectWiseModel):
    id: int | None
    accrual_type: AccrualType | None
    start_year: int | None
    end_year: int | None
    hours: float | None
    time_accrual: TimeAccrualReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True