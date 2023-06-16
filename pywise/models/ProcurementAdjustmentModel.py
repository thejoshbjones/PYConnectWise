from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AdjustmentTypeReferenceModel import AdjustmentTypeReferenceModel
from pywise.models.AdjustmentDetailModel import AdjustmentDetailModel

class ProcurementAdjustmentModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    type: AdjustmentTypeReferenceModel | None
    reason: str | None
    notes: str | None
    closed_flag: bool | None
    closed_by: str | None
    closed_date: str | None
    adjustment_details: list[AdjustmentDetailModel] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True