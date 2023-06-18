from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
from pywise.models.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
from pywise.models.IntegratorLoginReferenceModel import IntegratorLoginReferenceModel

class ManagementModel(ConnectWiseModel):
    id: int | None
    run_time: str | None
    added_configuration_status: ConfigurationStatusReferenceModel | None
    deleted_configuration_status: ConfigurationStatusReferenceModel | None
    integrator_login: IntegratorLoginReferenceModel | None
    schedule_executive_summary_report_flag: bool | None
    executive_summary_report_schedule_day: int | None
    executive_summary_report_schedule_hour: int | None
    executive_summary_report_schedule_minute: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True