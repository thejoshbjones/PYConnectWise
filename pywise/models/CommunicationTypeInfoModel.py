from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class CommunicationTypeInfoModel(ConnectWiseModel):
    id: int | None
    description: str | None
    phone_flag: bool | None
    fax_flag: bool | None
    email_flag: bool | None
    default_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True