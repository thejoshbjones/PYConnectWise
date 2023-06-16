from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel

class SalesTeamMemberModel(ConnectWiseModel):
    id: int | None
    member: MemberReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    allow_access_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True