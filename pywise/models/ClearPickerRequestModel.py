from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from enum import Enum
class ClearPickerRequestModelType(str, Enum):
    Company = 'Company'
    Vendor = 'Vendor'

class ClearPickerRequestModel(ConnectWiseModel):
    member: MemberReferenceModel | None
    type: ClearPickerRequestModelType | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True