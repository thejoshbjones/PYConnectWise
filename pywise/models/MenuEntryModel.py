from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MenuLocationReferenceModel import MenuLocationReferenceModel

class MenuEntryModel(ConnectWiseModel):
    id: int | None
    menu_location: MenuLocationReferenceModel | None
    caption: str | None
    link: str | None
    new_window_flag: bool | None
    location_ids: list[int] | None
    origin: str | None
    client_id: str | None
    add_all_locations: bool | None
    remove_all_locations: bool | None
    small_menu_icon_id: int | None
    large_menu_icon_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True