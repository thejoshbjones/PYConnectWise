from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class SsoUserModel(ConnectWiseModel):
    id: int | None
    sso_user_id: str | None
    user_name: str | None
    first_name: str | None
    last_name: str | None
    email: str | None
    email_confirmed: bool | None
    disabled_flag: bool | None
    linked_flag: bool | None
    date_entered: str | None
    last_updated: str | None
    linked_member: MemberReferenceModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True