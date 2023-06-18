from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.PortalConfigurationReferenceModel import PortalConfigurationReferenceModel

class PortalReportModel(ConnectWiseModel):
    id: int | None
    portal_configuration: PortalConfigurationReferenceModel | None
    name: str | None
    url: str | None
    open_same_window_flag: bool | None
    custom_flag: bool | None
    display_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True