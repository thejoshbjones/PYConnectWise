from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel

class ContactTrackModel(ConnectWiseModel):
    id: int | None
    track_id: int | None
    name: str | None
    start_date: str | None
    end_date: str | None
    action_taken: int | None
    action_remaining: int | None
    started_by: str | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True