from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel
from pyconnectwise.models.manage.ConfigurationTypeQuestionReferenceModel import ConfigurationTypeQuestionReferenceModel

class ConfigurationTypeQuestionValueModel(ConnectWiseModel):
    id: int
    configuration_type: ConfigurationTypeReferenceModel
    question: ConfigurationTypeQuestionReferenceModel
    value: str
    default_flag: bool
    inactive_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True