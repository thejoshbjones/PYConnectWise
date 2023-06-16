from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel

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