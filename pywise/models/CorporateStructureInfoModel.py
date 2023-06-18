from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class CorporateStructureInfoModel(ConnectWiseModel):
    id: int | None
    location_caption: str | None
    group_caption: str | None
    base_currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True