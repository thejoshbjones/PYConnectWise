from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel

class BoardTypeSubTypeItemAssociationModel(ConnectWiseModel):
    id: int | None
    type: ServiceTypeReferenceModel | None
    sub_type: ServiceSubTypeReferenceModel | None
    item: ServiceItemReferenceModel | None
    board: BoardReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True