from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from enum import Enum
class Language(str, Enum):
    English = 'English'
    Spanish = 'Spanish'
    French = 'French'
    British = 'British'
    Australian = 'Australian'
    BrazilianPortuguese = 'BrazilianPortuguese'
    CanadianFrench = 'CanadianFrench'
    German = 'German'
    NewZealand = 'NewZealand'
    Dutch = 'Dutch'

class PortalConfigurationModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    company: CompanyReferenceModel | None
    login_background_color: str | None
    portal_background_color: str | None
    menu_color: str | None
    button_color: str | None
    header_color: str | None
    url: str | None
    language: Language | None
    welcome_text: str | None
    board_ids: list[int] | None
    agreement_type_ids: list[int] | None
    config_type_ids: list[int] | None
    location_ids: list[int] | None
    portal_image_copy_success_flag: bool | None
    display_vendor_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True