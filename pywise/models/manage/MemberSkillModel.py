from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SkillReferenceModel import SkillReferenceModel
from enum import Enum
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
class SkillLevel(str, Enum):
    Beginner = 'Beginner'
    Intermediate = 'Intermediate'
    Advanced = 'Advanced'
    Expert = 'Expert'

class MemberSkillModel(ConnectWiseModel):
    id: int
    skill: SkillReferenceModel
    skill_level: SkillLevel
    certified_flag: bool
    years_experience: int
    notes: str
    member: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True