from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.KPICategoryReferenceModel import KPICategoryReferenceModel

class KPIModel(ConnectWiseModel):
    id: int | None
    name: str | None
    category: KPICategoryReferenceModel | None
    date_filter: str | None
    sort_order: int | None
    inactive_flag: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True