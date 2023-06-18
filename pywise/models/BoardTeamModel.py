from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class BoardTeamModel(ConnectWiseModel):
    id: int | None
    name: str | None
    team_leader: MemberReferenceModel | None
    members: list[int] | None
    default_flag: bool | None
    notify_on_ticket_delete: bool | None
    board_id: int | None
    location_id: int | None
    business_unit_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True