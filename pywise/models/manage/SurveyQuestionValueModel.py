from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SurveyReferenceModel import SurveyReferenceModel
from pywise.models.manage.SurveyQuestionReferenceModel import SurveyQuestionReferenceModel

class SurveyQuestionValueModel(ConnectWiseModel):
    id: int
    survey: SurveyReferenceModel
    question: SurveyQuestionReferenceModel
    value: str
    default_flag: bool
    point_value: int
    inactive_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True