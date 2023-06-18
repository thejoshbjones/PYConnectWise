from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ScheduleEntryReferenceModel import ScheduleEntryReferenceModel
from pywise.models.manage.ServiceCodeReferenceModel import ServiceCodeReferenceModel
from enum import Enum
class ChildScheduleAction(str, Enum):
    Transfer = 'Transfer'
    Delete = 'Delete'
    Done = 'Done'

class TicketTaskModel(ConnectWiseModel):
    id: int | None
    ticket_id: int | None
    notes: str | None
    closed_flag: bool | None
    priority: int | None
    schedule: ScheduleEntryReferenceModel | None
    code: ServiceCodeReferenceModel | None
    resolution: str | None
    child_schedule_action: ChildScheduleAction | None
    child_ticket_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True