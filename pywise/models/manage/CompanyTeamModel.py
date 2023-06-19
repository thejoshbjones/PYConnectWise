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
    id: int
    company: CompanyReferenceModel
    team_role: TeamRoleReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    contact: ContactReferenceModel
    member: MemberReferenceModel
    account_manager_flag: bool
    tech_flag: bool
    sales_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True