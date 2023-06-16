from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class WeekStart(str, Enum):
    Sunday = 'Sunday'
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'

class PortalCalendarModel(ConnectWiseModel):
    id: int | None
    week_start: WeekStart | None
    adjust1_start: str | None
    adjust1_end: str | None
    adjust1_hours: float | None
    adjust2_start: str | None
    adjust2_end: str | None
    adjust2_hours: float | None
    adjust3_start: str | None
    adjust3_end: str | None
    adjust3_hours: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True