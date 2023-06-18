from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from enum import Enum
class VacationAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'
class SickAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'
class PtoAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'
class HolidayAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'

class TimeAccrualModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    vacation_flag: bool | None
    vacation_available_type: VacationAvailableType | None
    vacation_carryover_allowed_flag: bool | None
    vacation_carryover_limit: float | None
    sick_flag: bool | None
    sick_available_type: SickAvailableType | None
    sick_carryover_allowed_flag: bool | None
    sick_carryover_limit: float | None
    pto_flag: bool | None
    pto_available_type: PtoAvailableType | None
    pto_carryover_allowed_flag: bool | None
    pto_carryover_limit: float | None
    holiday_flag: bool | None
    holiday_available_type: HolidayAvailableType | None
    holiday_carryover_allowed_flag: bool | None
    holiday_carryover_limit: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True