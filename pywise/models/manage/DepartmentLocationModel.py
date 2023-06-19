from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.LdapConfigurationReferenceModel import LdapConfigurationReferenceModel

class DepartmentLocationModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    department_manager: MemberReferenceModel
    dispatch: MemberReferenceModel
    service_manager: MemberReferenceModel
    duty_manager: MemberReferenceModel
    ldap_config: LdapConfigurationReferenceModel
    add_all_locations: bool
    remove_all_locations: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True