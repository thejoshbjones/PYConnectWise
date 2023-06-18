from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class AgreementBillingInfoModel(ConnectWiseModel):
    agreement_name: str | None
    agreement_type: str | None
    agreement_amount: float | None
    agreement_rec_id: int | None
    parent_rec_id: int | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True