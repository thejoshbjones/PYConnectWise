from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ValidationErrorModel import ValidationErrorModel

class ErrorResponseMessageModel(ConnectWiseModel):
    code: str
    message: str
    errors: list[ValidationErrorModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True