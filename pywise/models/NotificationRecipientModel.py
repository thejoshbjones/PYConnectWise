from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class NotificationRecipientModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    name: str | None
    external_flag: bool | None
    service_flag: bool | None
    sales_flag: bool | None
    invoice_flag: bool | None
    agreement_flag: bool | None
    member_flag: bool | None
    config_flag: bool | None
    msp_flag: bool | None
    track_flag: bool | None
    project_flag: bool | None
    procurement_flag: bool | None
    knowledge_base_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True