from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class EPayConfigurationModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    currency: CurrencyReferenceModel
    url: str
    store_identifier: str
    encryption_key: str
    initialization_vector: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True