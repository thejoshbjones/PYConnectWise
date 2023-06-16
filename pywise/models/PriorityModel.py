from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Color(str, Enum):
    Black = 'Black'
    Blue = 'Blue'
    Cyan = 'Cyan'
    Gray = 'Gray'
    Green = 'Green'
    Lime = 'Lime'
    Orange = 'Orange'
    Pink = 'Pink'
    Purple = 'Purple'
    Red = 'Red'
    White = 'White'
    Yellow = 'Yellow'
    Custom = 'Custom'

class PriorityModel(ConnectWiseModel):
    id: int | None
    name: str | None
    color: Color | None
    sort_order: int | None
    default_flag: bool | None
    image_link: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True