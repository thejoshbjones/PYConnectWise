from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pywise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel

class ConversionModel(ConnectWiseModel):
    id: int | None
    quantity: float | None
    uom_type: UnitOfMeasureReferenceModel | None
    parent_u_o_m: UnitOfMeasureReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True