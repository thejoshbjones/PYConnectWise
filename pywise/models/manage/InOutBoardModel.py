from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.InOutTypeReferenceModel import InOutTypeReferenceModel

class InOutBoardModel(ConnectWiseModel):
    id: int | None
    member: MemberReferenceModel | None
    in_out_type: InOutTypeReferenceModel | None
    additional_info: str | None
    date_back: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True