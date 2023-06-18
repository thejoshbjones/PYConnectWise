from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class EmailTokenModel(ConnectWiseModel):
    id: int | None
    token: str | None
    description: str | None
    address_flag: bool | None
    agreement_flag: bool | None
    company_flag: bool | None
    config_flag: bool | None
    contact_flag: bool | None
    invoice_flag: bool | None
    purchase_order_flag: bool | None
    purchase_order_status_flag: bool | None
    rma_flag: bool | None
    sales_flag: bool | None
    service_flag: bool | None
    tracks_flag: bool | None
    workflow_flag: bool | None
    portal_password_flag: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True