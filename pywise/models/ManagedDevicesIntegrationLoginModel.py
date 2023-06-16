from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

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