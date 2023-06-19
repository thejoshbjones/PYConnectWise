from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Identifier(str, Enum):
    QB99 = 'QB99'
    Mas200 = 'Mas200'
    GPlains = 'GPlains'
    SBA = 'SBA'
    Mas200v4 = 'Mas200v4'
    Other = 'Other'

class AccountingPackageReferenceModel(ConnectWiseModel):
    id: int
    identifier: Identifier
    name: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True