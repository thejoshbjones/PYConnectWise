from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.LicenseBitModel import LicenseBitModel

class InfoModel(ConnectWiseModel):
    version: str | None
    is_cloud: bool | None
    server_time_zone: str | None
    license_bits: list[LicenseBitModel] | None
    cloud_region: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True