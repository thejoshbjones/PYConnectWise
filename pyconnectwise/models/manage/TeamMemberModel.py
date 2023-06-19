from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class TeamMemberModel(ConnectWiseModel):
    id: int
    board: BoardReferenceModel
    team: ServiceTeamReferenceModel
    member: MemberReferenceModel
    team_leader_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True