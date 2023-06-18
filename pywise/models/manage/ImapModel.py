from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.EmailConnectorReferenceModel import EmailConnectorReferenceModel

class ImapModel(ConnectWiseModel):
    id: int | None
    name: str | None
    imap_name: str | None
    processed_name: str | None
    failed_folder: str | None
    server: str | None
    user_name: str | None
    password: str | None
    port: int | None
    ssl_flag: bool | None
    email_connector: EmailConnectorReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True