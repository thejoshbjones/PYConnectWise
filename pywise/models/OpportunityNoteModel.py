from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.NoteTypeReferenceModel import NoteTypeReferenceModel

class OpportunityNoteModel(ConnectWiseModel):
    id: int | None
    opportunity_id: int | None
    type: NoteTypeReferenceModel | None
    text: str | None
    flagged: bool | None
    entered_by: str | None
    mobile_guid: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True