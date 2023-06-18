from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.TeamRoleReferenceModel import TeamRoleReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

class CompanyTeamModel(ConnectWiseModel):
    id: int | None
    company: CompanyReferenceModel | None
    team_role: TeamRoleReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    contact: ContactReferenceModel | None
    member: MemberReferenceModel | None
    account_manager_flag: bool | None
    tech_flag: bool | None
    sales_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True