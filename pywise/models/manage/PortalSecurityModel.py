from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class PortalSecurityModel(ConnectWiseModel):
    identifier: str | None
    enabled: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True