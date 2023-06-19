from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pyconnectwise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pyconnectwise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel

class BoardTypeSubTypeItemAssociationModel(ConnectWiseModel):
    id: int
    type: ServiceTypeReferenceModel
    sub_type: ServiceSubTypeReferenceModel
    item: ServiceItemReferenceModel
    board: BoardReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True