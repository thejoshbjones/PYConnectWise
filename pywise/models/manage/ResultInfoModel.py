from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.IRestIdentifiedItemModel import IRestIdentifiedItemModel
from pywise.models.manage.ErrorResponseMessageModel import ErrorResponseMessageModel

class ResultInfoModel(ConnectWiseModel):
    success: bool | None
    original_index: int | None
    status_code: int | None
    data: IRestIdentifiedItemModel | None
    error: ErrorResponseMessageModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True