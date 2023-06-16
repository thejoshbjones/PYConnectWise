from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.HolidayListReferenceModel import HolidayListReferenceModel

class CalendarModel(ConnectWiseModel):
    id: int | None
    name: str | None
    holiday_list: HolidayListReferenceModel | None
    monday_start_time: str | None
    monday_end_time: str | None
    tuesday_start_time: str | None
    tuesday_end_time: str | None
    wednesday_start_time: str | None
    wednesday_end_time: str | None
    thursday_start_time: str | None
    thursday_end_time: str | None
    friday_start_time: str | None
    friday_end_time: str | None
    saturday_start_time: str | None
    saturday_end_time: str | None
    sunday_start_time: str | None
    sunday_end_time: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True