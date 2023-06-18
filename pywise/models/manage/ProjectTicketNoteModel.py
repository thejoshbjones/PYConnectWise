from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
class NoteType(str, Enum):
    TicketNote = 'TicketNote'
    TimeEntryNote = 'TimeEntryNote'
    MeetingNote = 'MeetingNote'

class ProjectTicketNoteModel(ConnectWiseModel):
    id: int | None
    note_type: NoteType | None
    ticket: TicketReferenceModel | None
    text: str | None
    detail_description_flag: bool | None
    internal_analysis_flag: bool | None
    resolution_flag: bool | None
    time_start: str | None
    time_end: str | None
    bundled_flag: bool | None
    merged_flag: bool | None
    issue_flag: bool | None
    original_author: str | None
    member: MemberReferenceModel | None
    contact: ContactReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True