from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class FormSubmittedModel(ConnectWiseModel):
    id: int | None
    campaign_id: int | None
    contact_id: int | None
    date_submitted: str | None
    url: str | None
    query_string: str | None
    page_type: str | None
    page_sub_type: str | None
    topic: str | None
    version: str | None
    status: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True