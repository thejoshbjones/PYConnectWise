from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class ValidationErrorModel(ConnectWiseModel):
    code: str | None
    message: str | None
    resource: str | None
    field: str | None
    details: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True