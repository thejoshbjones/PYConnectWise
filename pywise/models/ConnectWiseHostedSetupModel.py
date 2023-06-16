from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ConnectWiseHostedSetupModelType(str, Enum):
    Tab = 'Tab'
    Pod = 'Pod'
    ToolbarButton = 'ToolbarButton'

class ConnectWiseHostedSetupModel(ConnectWiseModel):
    id: int | None
    screen_id: int | None
    description: str | None
    url: str | None
    type: ConnectWiseHostedSetupModelType | None
    client_id: str | None
    origin: str | None
    pod_height: int | None
    toolbar_button_dialog_height: int | None
    toolbar_button_dialog_width: int | None
    toolbar_button_text: str | None
    toolbar_button_tool_tip: str | None
    toolbar_button_icon_document_id: int | None
    disabled_flag: bool | None
    location_ids: list[int] | None
    locations_enabled_flag: bool | None
    created_by: str | None
    date_created: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True