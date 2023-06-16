from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class WorkflowNotifyTypeModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    name: str | None
    is_setup_flag: bool | None
    external_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True