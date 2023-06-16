from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class SsoType(str, Enum):
    CWSSO = 'CWSSO'
    SAML = 'SAML'

class SsoConfigurationModel(ConnectWiseModel):
    id: int | None
    name: str | None
    sso_type: SsoType | None
    inactive_flag: bool | None
    saml_entity_id: str | None
    saml_sign_in_url: str | None
    saml_idp_certificate: str | None
    saml_certificate_name: str | None
    saml_certificate_issued_to: str | None
    saml_certificate_thumbprint: str | None
    saml_certificate_valid_from: str | None
    saml_certificate_valid_to: str | None
    location_ids: list[int] | None
    client_id: str | None
    sts_base_url: str | None
    sts_user_admin_url: str | None
    token: str | None
    submitted_member_count: int | None
    all_members_submitted: bool | None
    _info: dict[str, str] | None
    is_sso_on_by_default: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True