from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.WorkflowTableTypeReferenceModel import WorkflowTableTypeReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from enum import Enum
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
class BatchFrequencyUnit(str, Enum):
    Minutes = 'Minutes'
    Hours = 'Hours'
    Days = 'Days'
class BatchSchedule(str, Enum):
    AnyTime = 'AnyTime'
    MyCompanyOfficeHours = 'MyCompanyOfficeHours'
    SlaHours = 'SlaHours'

class WorkflowModel(ConnectWiseModel):
    id: int
    name: str
    table_type: WorkflowTableTypeReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    activate_flag: bool
    batch_interval: int
    batch_frequency_unit: BatchFrequencyUnit
    batch_last_ran: str
    batch_schedule: BatchSchedule
    board: BoardReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True