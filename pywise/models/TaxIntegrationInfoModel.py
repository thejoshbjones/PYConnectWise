from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class TaxIntegrationType(str, Enum):
    Avalara = 'Avalara'

class TaxIntegrationInfoModel(ConnectWiseModel):
    id: int | None
    enabled_flag: bool | None
    tax_integration_type: TaxIntegrationType | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True