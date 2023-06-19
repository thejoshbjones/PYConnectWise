from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel

class ConversionModel(ConnectWiseModel):
    id: int
    quantity: float
    uom_type: UnitOfMeasureReferenceModel
    parent_u_o_m: UnitOfMeasureReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True