from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class PortalConfigurationPasswordEmailSetupModel(ConnectWiseModel):
    id: int | None
    valid_password_email_use_custom_email_flag: bool | None
    valid_password_email_from_first_name: str | None
    valid_password_email_from_last_name: str | None
    valid_password_email_from_email: str | None
    valid_password_email_subject: str | None
    valid_password_email_body: str | None
    invalid_password_email_use_custom_email_flag: bool | None
    invalid_password_email_from_first_name: str | None
    invalid_password_email_from_last_name: str | None
    invalid_password_email_from_email: str | None
    invalid_password_email_subject: str | None
    invalid_password_email_body: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True