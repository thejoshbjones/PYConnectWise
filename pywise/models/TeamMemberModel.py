from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class TeamMemberModel(ConnectWiseModel):
    id: int | None
    board: BoardReferenceModel | None
    team: ServiceTeamReferenceModel | None
    member: MemberReferenceModel | None
    team_leader_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True