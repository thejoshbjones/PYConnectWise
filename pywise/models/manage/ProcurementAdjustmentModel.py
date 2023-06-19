from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.AdjustmentTypeReferenceModel import AdjustmentTypeReferenceModel
from pywise.models.manage.AdjustmentDetailModel import AdjustmentDetailModel

class ProcurementAdjustmentModel(ConnectWiseModel):
    id: int
    identifier: str
    type: AdjustmentTypeReferenceModel
    reason: str
    notes: str
    closed_flag: bool
    closed_by: str
    closed_date: str
    adjustment_details: list[AdjustmentDetailModel]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True