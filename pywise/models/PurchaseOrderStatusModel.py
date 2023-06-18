from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.PurchaseOrderStatusEmailTemplateReferenceModel import PurchaseOrderStatusEmailTemplateReferenceModel

class PurchaseOrderStatusModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    closed_flag: bool | None
    inactive_flag: bool | None
    default_closed_flag: bool | None
    sort_order: int | None
    email_template: PurchaseOrderStatusEmailTemplateReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True