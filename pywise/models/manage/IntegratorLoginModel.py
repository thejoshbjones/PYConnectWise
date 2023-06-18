from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

class IntegratorLoginModel(ConnectWiseModel):
    id: int | None
    username: str | None
    password: str | None
    can_access_all_records_flag: bool | None
    can_access_all_apis_flag: bool | None
    inactive_flag: bool | None
    date_inactivated: str | None
    inactivated_by: MemberReferenceModel | None
    service_ticket_api_flag: bool | None
    board: BoardReferenceModel | None
    service_board_callback_url: str | None
    service_board_legacy_callback_flag: bool | None
    time_entry_api_flag: bool | None
    member: MemberReferenceModel | None
    time_entry_callback_url: str | None
    time_entry_legacy_callback_flag: bool | None
    managed_services_api_flag: bool | None
    managed_services_auto_child_flag: bool | None
    managed_services_childing_flag: bool | None
    contact_api_flag: bool | None
    contact_callback_url: str | None
    contact_legacy_callback_flag: bool | None
    company_api_flag: bool | None
    company_callback_url: str | None
    company_legacy_callback_flag: bool | None
    activity_api_flag: bool | None
    activity_callback_url: str | None
    activity_legacy_callback_flag: bool | None
    invoice_api_flag: bool | None
    product_api_flag: bool | None
    product_callback_url: str | None
    product_legacy_callback_flag: bool | None
    opportunity_api_flag: bool | None
    opportunity_callback_url: str | None
    opportunity_legacy_callback_flag: bool | None
    opportunity_conversion_api_flag: bool | None
    member_api_flag: bool | None
    marketing_api_flag: bool | None
    purchasing_api_flag: bool | None
    purchasing_callback_url: str | None
    purchasing_legacy_callback_flag: bool | None
    reporting_api_flag: bool | None
    system_api_flag: bool | None
    project_api_flag: bool | None
    project_callback_url: str | None
    project_legacy_callback_flag: bool | None
    configuration_api_flag: bool | None
    configuration_auto_child_flag: bool | None
    configuration_childling_flag: bool | None
    configuration_callback_url: str | None
    configuration_legacy_callback_flag: bool | None
    schedule_api_flag: bool | None
    schedule_callback_url: str | None
    schedule_legacy_callback_flag: bool | None
    agreement_api_flag: bool | None
    agreement_callback_url: str | None
    agreement_callback_legacy_flag: bool | None
    document_api_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True