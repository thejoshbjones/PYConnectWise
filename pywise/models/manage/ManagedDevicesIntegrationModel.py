from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.IntegratorLoginReferenceModel import IntegratorLoginReferenceModel
class LoginBy(str, Enum):
    Global = 'Global'
    Member = 'Member'
class DefaultBillingLevel(str, Enum):
    Detail = 'Detail'
    Summary = 'Summary'

class ManagedDevicesIntegrationModel(ConnectWiseModel):
    id: int | None
    name: str | None
    solution: str | None
    portal_url: str | None
    login_by: LoginBy | None
    global_login_username: str | None
    global_login_password: str | None
    default_billing_level: DefaultBillingLevel | None
    management_it_setup_type: str | None
    default_location: SystemLocationReferenceModel | None
    default_department: SystemDepartmentReferenceModel | None
    integrator_login: IntegratorLoginReferenceModel | None
    match_on_serial_number_flag: bool | None
    disable_new_cross_references_flag: bool | None
    config_bill_customer_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True