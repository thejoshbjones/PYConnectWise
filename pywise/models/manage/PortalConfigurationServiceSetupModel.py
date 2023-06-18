from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.ServiceSignoffReferenceModel import ServiceSignoffReferenceModel
from pywise.models.manage.ServiceSignoffReferenceModel import ServiceSignoffReferenceModel
class DisplayClosedTicketsOption(str, Enum):
    DoNotDisplay = 'DoNotDisplay'
    Closed30Days = 'Closed30Days'
    Closed60Days = 'Closed60Days'
    Closed90Days = 'Closed90Days'
    Closed120Days = 'Closed120Days'
    AllClosed = 'AllClosed'

class PortalConfigurationServiceSetupModel(ConnectWiseModel):
    id: int | None
    service_type_flag: bool | None
    service_sub_type_flag: bool | None
    service_sub_type_item_flag: bool | None
    status_flag: bool | None
    site_name_flag: bool | None
    entered_date_flag: bool | None
    last_update_flag: bool | None
    required_date_flag: bool | None
    contact_flag: bool | None
    assigned_resources_flag: bool | None
    sla_info_flag: bool | None
    service_board_flag: bool | None
    budget_hours_flag: bool | None
    actual_hours_flag: bool | None
    approval_status_flag: bool | None
    open_tasks_flag: bool | None
    closed_tasks_flag: bool | None
    enable_chat_assist_flag: bool | None
    display_closed_tickets_option: DisplayClosedTicketsOption | None
    time_materials_ticket_template: ServiceSignoffReferenceModel | None
    fixed_fee_ticket_template: ServiceSignoffReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True