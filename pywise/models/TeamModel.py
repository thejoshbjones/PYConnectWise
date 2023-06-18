from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SalesTeamReferenceModel import SalesTeamReferenceModel
class TeamModelType(str, Enum):
    Individual = 'Individual'
    Team = 'Team'

class TeamModel(ConnectWiseModel):
    id: int | None
    type: TeamModelType | None
    member: MemberReferenceModel | None
    sales_team: SalesTeamReferenceModel | None
    commission_percent: int | None
    referral_flag: bool | None
    opportunity_id: int | None
    responsible_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True