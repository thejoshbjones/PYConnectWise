from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.NoteTypeReferenceModel import NoteTypeReferenceModel

class ProjectNoteModel(ConnectWiseModel):
    id: int | None
    project_id: int | None
    text: str | None
    type: NoteTypeReferenceModel | None
    flagged: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True