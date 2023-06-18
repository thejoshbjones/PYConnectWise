from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

class ManagedDevicesIntegrationLoginModel(ConnectWiseModel):
    id: int | None
    managed_devices_integration: ManagedDevicesIntegrationReferenceModel | None
    username: str | None
    password: str | None
    member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True