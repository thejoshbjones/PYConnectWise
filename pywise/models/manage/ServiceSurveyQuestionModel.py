from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.ServiceSurveyQuestionOptionModel import ServiceSurveyQuestionOptionModel
class ServiceSurveyQuestionModelType(str, Enum):
    OpenEnded = 'OpenEnded'
    Selection = 'Selection'

class ServiceSurveyQuestionModel(ConnectWiseModel):
    id: int
    sequence_number: int
    type: ServiceSurveyQuestionModelType
    question: str
    options: list[ServiceSurveyQuestionOptionModel]
    include_flag: bool
    required_flag: bool
    no_answer_points: int
    survey_id: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True