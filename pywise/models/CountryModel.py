from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.AddressFormatReferenceModel import AddressFormatReferenceModel

class CountryModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    currency: CurrencyReferenceModel | None
    city_caption: str | None
    state_caption: str | None
    zip_caption: str | None
    zip_minimum_length: int | None
    dialing_prefix: str | None
    address_format: AddressFormatReferenceModel | None
    country_code: str | None
    localization_caption_one: str | None
    localization_value_one: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True