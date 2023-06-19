from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.InOutTypeReferenceModel import InOutTypeReferenceModel

class InOutBoardModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    in_out_type: InOutTypeReferenceModel
    additional_info: str
    date_back: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True