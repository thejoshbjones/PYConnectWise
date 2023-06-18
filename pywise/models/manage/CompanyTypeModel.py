from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CompanyTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    vendor_flag: bool | None
    service_alert_flag: bool | None
    service_alert_message: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True