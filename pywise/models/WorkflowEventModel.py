from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class FrequencyUnit(str, Enum):
    Minutes = 'Minutes'
    Hours = 'Hours'
    Days = 'Days'
    Months = 'Months'
class ExecutionTime(str, Enum):
    Once = 'Once'
    MultipleTimes = 'MultipleTimes'
    Continuously = 'Continuously'

class WorkflowEventModel(ConnectWiseModel):
    id: int | None
    name: str | None
    event_condition: str | None
    frequency_unit: FrequencyUnit | None
    frequency_of_execution: int | None
    max_number_of_execution: int | None
    execution_time: ExecutionTime | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True