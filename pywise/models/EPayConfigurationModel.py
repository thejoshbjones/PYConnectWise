from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class EPayConfigurationModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    currency: CurrencyReferenceModel | None
    url: str | None
    store_identifier: str | None
    encryption_key: str | None
    initialization_vector: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True