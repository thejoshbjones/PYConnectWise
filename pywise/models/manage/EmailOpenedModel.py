from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class EmailOpenedModel(ConnectWiseModel):
    id: int | None
    campaign_id: int | None
    contact_id: int | None
    date_opened: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True