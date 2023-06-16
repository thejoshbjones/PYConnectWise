from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.OrderStatusReferenceModel import OrderStatusReferenceModel

class OrderStatusEmailTemplateModel(ConnectWiseModel):
    id: int | None
    status: OrderStatusReferenceModel | None
    use_sender_flag: bool | None
    first_name: str | None
    last_name: str | None
    email_address: str | None
    subject: str | None
    body: str | None
    copy_sender_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True