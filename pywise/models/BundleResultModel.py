from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.IRestIdentifiedItemModel import IRestIdentifiedItemModel
from pywise.models.ErrorResponseMessageModel import ErrorResponseMessageModel

class BundleResultModel(ConnectWiseModel):
    sequence_number: int | None
    resource_type: str | None
    entities: list[IRestIdentifiedItemModel] | None
    count: int | None
    version: str | None
    success: bool | None
    status_code: int | None
    error: ErrorResponseMessageModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True