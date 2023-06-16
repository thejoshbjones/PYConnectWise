from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class ContactTypeModel(ConnectWiseModel):
    id: int | None
    description: str | None
    default_flag: bool | None
    service_alert_flag: bool | None
    service_alert_message: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True