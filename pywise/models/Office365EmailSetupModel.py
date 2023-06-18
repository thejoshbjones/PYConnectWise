from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.EmailConnectorReferenceModel import EmailConnectorReferenceModel

class Office365EmailSetupModel(ConnectWiseModel):
    id: int | None
    name: str | None
    username: str | None
    inbox_folder: str | None
    processed_folder: str | None
    failed_folder: str | None
    tenant_id: str | None
    client_id: str | None
    client_secret: str | None
    authorized_flag: bool | None
    inactive_flag: bool | None
    email_connector: EmailConnectorReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True