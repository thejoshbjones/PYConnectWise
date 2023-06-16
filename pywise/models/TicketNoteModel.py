from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel

class TicketNoteModel(ConnectWiseModel):
    id: int | None
    ticket_id: int | None
    text: str | None
    detail_description_flag: bool | None
    internal_analysis_flag: bool | None
    resolution_flag: bool | None
    issue_flag: bool | None
    member: MemberReferenceModel | None
    contact: ContactReferenceModel | None
    customer_updated_flag: bool | None
    process_notifications: bool | None
    internal_flag: bool | None
    external_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True