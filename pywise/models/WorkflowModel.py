from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.WorkflowTableTypeReferenceModel import WorkflowTableTypeReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from enum import Enum
from pywise.models.BoardReferenceModel import BoardReferenceModel
class BatchFrequencyUnit(str, Enum):
    Minutes = 'Minutes'
    Hours = 'Hours'
    Days = 'Days'
class BatchSchedule(str, Enum):
    AnyTime = 'AnyTime'
    MyCompanyOfficeHours = 'MyCompanyOfficeHours'
    SlaHours = 'SlaHours'

class WorkflowModel(ConnectWiseModel):
    id: int | None
    name: str | None
    table_type: WorkflowTableTypeReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    activate_flag: bool | None
    batch_interval: int | None
    batch_frequency_unit: BatchFrequencyUnit | None
    batch_last_ran: str | None
    batch_schedule: BatchSchedule | None
    board: BoardReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True