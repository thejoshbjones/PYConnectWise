from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ScreenLink(str, Enum):
    Company = 'Company'
    Contact = 'Contact'
    Service = 'Service'
    Invoice = 'Invoice'
    PurchaseOrder = 'PurchaseOrder'
    SalesOrder = 'SalesOrder'

class LinkModel(ConnectWiseModel):
    id: int | None
    name: str | None
    table_reference_id: int | None
    url: str | None
    screen_link: ScreenLink | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True