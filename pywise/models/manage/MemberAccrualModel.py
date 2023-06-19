from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
class AccrualType(str, Enum):
    Holiday = 'Holiday'
    PTO = 'PTO'
    Sick = 'Sick'
    Vacation = 'Vacation'

class MemberAccrualModel(ConnectWiseModel):
    id: int
    accrual_type: AccrualType
    year: int
    hours: float
    reason: str
    member: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True