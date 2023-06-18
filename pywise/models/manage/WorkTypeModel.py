from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'
class AccrualType(str, Enum):
    Holiday = 'Holiday'
    PTO = 'PTO'
    Sick = 'Sick'
    Vacation = 'Vacation'

class WorkTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    bill_time: BillTime | None
    rate_type: RateType | None
    rate: float | None
    hours_min: float | None
    hours_max: float | None
    round_bill_hours_to: float | None
    accrual_type: AccrualType | None
    inactive_flag: bool | None
    overall_default_flag: bool | None
    activity_default_flag: bool | None
    utilization_flag: bool | None
    cost_multiplier: float | None
    integration_x_ref: str | None
    add_all_agreement_exclusions: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True