from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemMenuEntryReferenceModel import SystemMenuEntryReferenceModel

class MenuEntryLocationModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    menu_entry: SystemMenuEntryReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True