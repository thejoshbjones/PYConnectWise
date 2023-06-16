from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CallbackEntryModel(ConnectWiseModel):
    id: int | None
    description: str | None
    url: str | None
    object_id: int | None
    type: str | None
    level: str | None
    member_id: int | None
    payload_version: str | None
    inactive_flag: bool | None
    is_soap_callback_flag: bool | None
    is_self_suppressed_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True