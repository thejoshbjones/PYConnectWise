from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.UserDefinedFieldReferenceModel import UserDefinedFieldReferenceModel

class WorkflowTriggerOptionModel(ConnectWiseModel):
    value: str | None
    name: str | None
    custom_field: UserDefinedFieldReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True