from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
class AddLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'
class EditLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'
class DeleteLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'
class InquireLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'

class MySecurityModel(ConnectWiseModel):
    id: int | None
    add_level: AddLevel | None
    edit_level: EditLevel | None
    delete_level: DeleteLevel | None
    inquire_level: InquireLevel | None
    module_function_name: str | None
    module_function_description: str | None
    my_all_flag: bool | None
    module_function_identifier: str | None
    report_flag: bool | None
    restrict_flag: bool | None
    custom_flag: bool | None
    module_description: str | None
    module_identifier: str | None
    module_name: str | None
    sort_order: int | None
    member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True