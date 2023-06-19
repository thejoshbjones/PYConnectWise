from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.PurchaseOrderStatusReferenceModel import PurchaseOrderStatusReferenceModel

class PurchaseOrderStatusEmailTemplateModel(ConnectWiseModel):
    id: int
    status: PurchaseOrderStatusReferenceModel
    use_sender_flag: bool
    first_name: str
    last_name: str
    email_address: str
    subject: str
    body: str
    copy_sender_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True