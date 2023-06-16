from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
class BasedOn(str, Enum):
    AllHours = 'AllHours'
    Customer = 'Customer'
    MyCalendar = 'MyCalendar'
    Custom = 'Custom'

class SLAModel(ConnectWiseModel):
    id: int | None
    name: str | None
    based_on: BasedOn | None
    custom_calendar: CalendarReferenceModel | None
    default_flag: bool | None
    application_order: int | None
    hi_impact_hi_urgency: PriorityReferenceModel | None
    hi_impact_med_urgency: PriorityReferenceModel | None
    hi_impact_low_urgency: PriorityReferenceModel | None
    med_impact_hi_urgency: PriorityReferenceModel | None
    med_impact_med_urgency: PriorityReferenceModel | None
    med_impact_low_urgency: PriorityReferenceModel | None
    low_impact_hi_urgency: PriorityReferenceModel | None
    low_impact_med_urgency: PriorityReferenceModel | None
    low_impact_low_urgency: PriorityReferenceModel | None
    respond_hours: float | None
    respond_percent: int | None
    plan_within: float | None
    plan_within_percent: int | None
    resolution_hours: float | None
    resolution_percent: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True