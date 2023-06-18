from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CountryReferenceModel import CountryReferenceModel

class StateInfoModel(ConnectWiseModel):
    id: int | None
    name: str | None
    identifier: str | None
    country: CountryReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True