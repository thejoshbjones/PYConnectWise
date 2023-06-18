from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ManagementItSolutionType(str, Enum):
    LevelPlatforms = 'LevelPlatforms'
    NAble = 'NAble'
    Continuum = 'Continuum'
    Custom = 'Custom'

class ManagementItSolutionModel(ConnectWiseModel):
    id: int | None
    name: str | None
    management_it_solution_type: ManagementItSolutionType | None
    management_solution_name: str | None
    management_server_url: str | None
    webservice_override_url: str | None
    portal_override_login_url: str | None
    global_login_flag: bool | None
    global_login_username: str | None
    global_login_password: str | None
    using_ssl_flag: bool | None
    n_able_username: str | None
    n_able_password: str | None
    override_web_service_location_flag: bool | None
    override_login_location_flag: bool | None
    continuum_api_username: str | None
    continuum_api_password: str | None
    level_api_username: str | None
    level_api_password: str | None
    level_var_domain: str | None
    no_display_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True