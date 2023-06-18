from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

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