from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Module(str, Enum):
    Companies = 'Companies'
    Finance = 'Finance'
    Marketing = 'Marketing'
    Procurement = 'Procurement'
    Project = 'Project'
    Sales = 'Sales'
    ServiceDesk = 'ServiceDesk'
    TimeExpense = 'TimeExpense'

class CustomReportModel(ConnectWiseModel):
    id: int | None
    report_link: str | None
    name: str | None
    module: Module | None
    description: str | None
    generated_flag: bool | None
    parameter_prefix: str | None
    parameter_separator: str | None
    parameter_name_separator: str | None
    parameter_suffix: str | None
    location_flag: bool | None
    location_param_id: int | None
    location_default_flag: bool | None
    location_override: str | None
    department_flag: bool | None
    department_param_id: int | None
    department_default_flag: bool | None
    department_override: str | None
    territory_flag: bool | None
    territory_param_id: int | None
    territory_default_flag: bool | None
    territory_override: str | None
    company_flag: bool | None
    company_param_id: int | None
    company_override: str | None
    member_flag: bool | None
    member_param_id: int | None
    member_override: str | None
    start_date_flag: bool | None
    start_date_param_id: int | None
    start_date_override: str | None
    end_date_flag: bool | None
    end_date_param_id: int | None
    end_date_override: str | None
    opp_type_flag: bool | None
    opp_type_param_id: int | None
    opp_type_override: str | None
    opportunity_flag: bool | None
    opportunity_param_id: int | None
    opportunity_override: str | None
    marketing_campaign_flag: bool | None
    marketing_campaign_param_id: int | None
    marketing_campaign_override: str | None
    service_board_flag: bool | None
    service_board_param_id: int | None
    service_board_default_flag: bool | None
    service_board_override: str | None
    service_type_flag: bool | None
    service_type_param_id: int | None
    service_type_override: str | None
    service_status_flag: bool | None
    service_status_param_id: int | None
    service_status_override: str | None
    agreement_type_flag: bool | None
    agreement_type_param_id: int | None
    agreement_type_override: str | None
    agreement_flag: bool | None
    agreement_param_id: int | None
    agreement_override: str | None
    project_type_flag: bool | None
    project_type_param_id: int | None
    project_type_override: str | None
    project_flag: bool | None
    project_param_id: int | None
    project_override: str | None
    work_role_flag: bool | None
    work_role_param_id: int | None
    work_role_override: str | None
    work_type_flag: bool | None
    work_type_param_id: int | None
    work_type_override: str | None
    invoice_flag: bool | None
    invoice_param_id: int | None
    invoice_override: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True