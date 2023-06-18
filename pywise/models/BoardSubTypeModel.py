from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.BoardReferenceModel import BoardReferenceModel

class BoardSubTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    inactive_flag: bool | None
    type_association_ids: list[int] | None
    add_all_types_flag: bool | None
    remove_all_types_flag: bool | None
    board: BoardReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True