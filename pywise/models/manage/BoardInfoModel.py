from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from enum import Enum
class ProblemSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class InternalAnalysisSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class ResolutionSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class AllSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'

class BoardInfoModel(ConnectWiseModel):
    id: int | None
    name: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    project_flag: bool | None
    inactive_flag: bool | None
    closed_loop_discussions_flag: bool | None
    closed_loop_internal_analysis_flag: bool | None
    closed_loop_resolution_flag: bool | None
    closed_loop_all_flag: bool | None
    problem_sort: ProblemSort | None
    internal_analysis_sort: InternalAnalysisSort | None
    resolution_sort: ResolutionSort | None
    all_sort: AllSort | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True