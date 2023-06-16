from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SkillReferenceModel import SkillReferenceModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
class SkillLevel(str, Enum):
    Beginner = 'Beginner'
    Intermediate = 'Intermediate'
    Advanced = 'Advanced'
    Expert = 'Expert'

class MemberSkillModel(ConnectWiseModel):
    id: int | None
    skill: SkillReferenceModel | None
    skill_level: SkillLevel | None
    certified_flag: bool | None
    years_experience: int | None
    notes: str | None
    member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True