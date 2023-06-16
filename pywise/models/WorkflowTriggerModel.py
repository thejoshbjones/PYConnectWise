from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.UserDefinedFieldReferenceModel import UserDefinedFieldReferenceModel

class WorkflowTriggerModel(ConnectWiseModel):
    id: int | None
    name: str | None
    description: str | None
    has_options_flag: bool | None
    has_operator_flag: bool | None
    custom_field: UserDefinedFieldReferenceModel | None
    expected_type: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True