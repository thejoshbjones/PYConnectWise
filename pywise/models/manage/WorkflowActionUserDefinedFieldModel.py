from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class WorkflowActionUserDefinedFieldModel(ConnectWiseModel):
    id: int | None
    event_id: int | None
    action_id: int | None
    caption: str | None
    user_defined_field_id: int | None
    value: str | None
    overwrite_flag: bool | None
    pod_description: str | None
    field_type_id: str | None
    entry_type_id: str | None
    required_flag: bool | None
    inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True