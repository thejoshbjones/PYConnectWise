from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class MemberSsoSettingsReferenceModel(ConnectWiseModel):
    id: int | None
    sso_user_id: str | None
    user_name: str | None
    email: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True