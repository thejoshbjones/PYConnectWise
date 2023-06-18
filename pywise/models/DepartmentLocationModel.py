from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.LdapConfigurationReferenceModel import LdapConfigurationReferenceModel

class DepartmentLocationModel(ConnectWiseModel):
    id: int | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    department_manager: MemberReferenceModel | None
    dispatch: MemberReferenceModel | None
    service_manager: MemberReferenceModel | None
    duty_manager: MemberReferenceModel | None
    ldap_config: LdapConfigurationReferenceModel | None
    add_all_locations: bool | None
    remove_all_locations: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True