from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ScheduleEntryReferenceModel import ScheduleEntryReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class ScheduleDetailModel(ConnectWiseModel):
    id: int | None
    schedule_entry: ScheduleEntryReferenceModel | None
    date_start: str | None
    date_end: str | None
    member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True