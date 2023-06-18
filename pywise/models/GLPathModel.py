from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class GLPathModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    path: str | None
    sql_server_name: str | None
    database_name: str | None
    last_payment_sync: str | None
    last_payment_sync_by: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True