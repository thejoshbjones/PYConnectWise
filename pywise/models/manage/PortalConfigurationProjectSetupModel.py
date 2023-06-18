from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.PortalConfigurationReferenceModel import PortalConfigurationReferenceModel
from enum import Enum
class OnlyDisplay(str, Enum):
    DoNotDisplay = 'DoNotDisplay'
    Closed30Days = 'Closed30Days'
    Closed60Days = 'Closed60Days'
    Closed90Days = 'Closed90Days'
    Closed120Days = 'Closed120Days'
    AllClosed = 'AllClosed'

class PortalConfigurationProjectSetupModel(ConnectWiseModel):
    id: int | None
    portal_config: PortalConfigurationReferenceModel | None
    project_name_flag: bool | None
    project_type_flag: bool | None
    status_flag: bool | None
    project_manager_flag: bool | None
    billing_method_flag: bool | None
    contact_flag: bool | None
    estimated_start_flag: bool | None
    estimated_end_flag: bool | None
    description_flag: bool | None
    last_updated_flag: bool | None
    only_display: OnlyDisplay | None
    time_material_budget_hrs_flag: bool | None
    time_material_scheduled_start_flag: bool | None
    time_material_scheduled_finish_flag: bool | None
    time_material_scheduled_hrs_flag: bool | None
    time_material_actual_start_flag: bool | None
    time_material_actual_finish_flag: bool | None
    time_material_actual_hrs_flag: bool | None
    time_material_bill_flag: bool | None
    time_material_status_flag: bool | None
    time_material_assigned_flag: bool | None
    fixed_fee_budget_hrs_flag: bool | None
    fixed_fee_scheduled_start_flag: bool | None
    fixed_fee_scheduled_finish_flag: bool | None
    fixed_fee_scheduled_hrs_flag: bool | None
    fixed_fee_actual_start_flag: bool | None
    fixed_fee_actual_finish_flag: bool | None
    fixed_fee_actual_hrs_flag: bool | None
    fixed_fee_bill_flag: bool | None
    fixed_fee_status_flag: bool | None
    fixed_fee_assigned_flag: bool | None
    project_issue_budget_hrs_flag: bool | None
    project_issue_scheduled_start_flag: bool | None
    project_issue_scheduled_finish_flag: bool | None
    project_issue_scheduled_hrs_flag: bool | None
    project_issue_actual_start_flag: bool | None
    project_issue_actual_finish_flag: bool | None
    project_issue_actual_hrs_flag: bool | None
    project_issue_bill_flag: bool | None
    project_issue_status_flag: bool | None
    project_issue_assigned_flag: bool | None
    project_detail_total_hours_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True