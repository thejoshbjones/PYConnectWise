from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.TrackReferenceModel import TrackReferenceModel

class CompanyStatusModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    inactive_flag: bool | None
    notify_flag: bool | None
    disallow_saving_flag: bool | None
    notification_message: str | None
    custom_note_flag: bool | None
    cancel_open_tracks_flag: bool | None
    track: TrackReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True