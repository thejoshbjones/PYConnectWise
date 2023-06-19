from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
class BasedOn(str, Enum):
    AllHours = 'AllHours'
    Customer = 'Customer'
    MyCalendar = 'MyCalendar'
    Custom = 'Custom'

class SLAModel(ConnectWiseModel):
    id: int
    name: str
    based_on: BasedOn
    custom_calendar: CalendarReferenceModel
    default_flag: bool
    application_order: int
    hi_impact_hi_urgency: PriorityReferenceModel
    hi_impact_med_urgency: PriorityReferenceModel
    hi_impact_low_urgency: PriorityReferenceModel
    med_impact_hi_urgency: PriorityReferenceModel
    med_impact_med_urgency: PriorityReferenceModel
    med_impact_low_urgency: PriorityReferenceModel
    low_impact_hi_urgency: PriorityReferenceModel
    low_impact_med_urgency: PriorityReferenceModel
    low_impact_low_urgency: PriorityReferenceModel
    respond_hours: float
    respond_percent: int
    plan_within: float
    plan_within_percent: int
    resolution_hours: float
    resolution_percent: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True