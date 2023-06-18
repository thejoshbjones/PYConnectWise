from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.GenericIdIdentifierReferenceModel import GenericIdIdentifierReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class ServiceSurveyModel(ConnectWiseModel):
    id: int | None
    name: str | None
    inactive_flag: bool | None
    header_include_logo_flag: bool | None
    header_text: str | None
    header_text_visible_flag: bool | None
    footer_text: str | None
    footer_text_visible_flag: bool | None
    thank_you_text: str | None
    notify_who: GenericIdIdentifierReferenceModel | None
    notify_who_visible_flag: bool | None
    notify_member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True