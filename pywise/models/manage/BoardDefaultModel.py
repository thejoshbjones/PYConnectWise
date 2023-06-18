from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel

class BoardDefaultModel(ConnectWiseModel):
    id: int | None
    board: BoardReferenceModel | None
    service_type: ServiceTypeReferenceModel | None
    default_flag: bool | None
    agreement_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True