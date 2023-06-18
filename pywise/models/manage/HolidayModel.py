from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.HolidayListReferenceModel import HolidayListReferenceModel

class HolidayModel(ConnectWiseModel):
    id: int | None
    name: str | None
    all_day_flag: bool | None
    date: str | None
    time_start: str | None
    time_end: str | None
    holiday_list: HolidayListReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True