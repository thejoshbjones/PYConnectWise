from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class DeliveryMethodModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    email_flag: bool | None
    integration_email_flag: bool | None
    integration_print_flag: bool | None
    integration_active_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True