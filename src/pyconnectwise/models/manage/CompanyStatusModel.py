from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.TrackReferenceModel import TrackReferenceModel

class CompanyStatusModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    inactive_flag: bool
    notify_flag: bool
    disallow_saving_flag: bool
    notification_message: str
    custom_note_flag: bool
    cancel_open_tracks_flag: bool
    track: TrackReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True