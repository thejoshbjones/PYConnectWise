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
    id: int | None
    sequence_number: int | None
    type: ServiceSurveyQuestionModelType | None
    question: str | None
    options: list[ServiceSurveyQuestionOptionModel] | None
    include_flag: bool | None
    required_flag: bool | None
    no_answer_points: int | None
    survey_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True