from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ValidationErrorModel import ValidationErrorModel

class ErrorResponseMessageModel(ConnectWiseModel):
    code: str | None
    message: str | None
    errors: list[ValidationErrorModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True