from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class AdjustmentModel(ConnectWiseModel):
    id: int | None
    amount: float | None
    description: str | None
    effective_date: str | None
    agreement_id: int | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True