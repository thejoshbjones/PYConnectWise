from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class PeriodApplyTo(str, Enum):
    Both = 'Both'
    Expense = 'Expense'
    Time = 'Time'
class TimePeriodSetupModelType(str, Enum):
    Weekly = 'Weekly'
    BiWeekly = 'BiWeekly'
    SemiMonthly = 'SemiMonthly'
    Monthly = 'Monthly'

class TimePeriodSetupModel(ConnectWiseModel):
    id: int | None
    period_apply_to: PeriodApplyTo | None
    year: int | None
    number_future_periods: int | None
    type: TimePeriodSetupModelType | None
    description: str | None
    first_period_end_date: str | None
    monthly_period_ends: int | None
    semi_monthly_first_period: int | None
    semi_monthly_second_period: int | None
    semi_monthly_last_day_flag: bool | None
    last_day_flag: bool | None
    days_past_end_date: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True