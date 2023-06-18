from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SurveyReferenceModel import SurveyReferenceModel
from pywise.models.manage.SurveyQuestionReferenceModel import SurveyQuestionReferenceModel

class SurveyQuestionValueModel(ConnectWiseModel):
    id: int | None
    survey: SurveyReferenceModel | None
    question: SurveyQuestionReferenceModel | None
    value: str | None
    default_flag: bool | None
    point_value: int | None
    inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True