from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

class PortalConfigurationOpportunitySetupModel(ConnectWiseModel):
    id: int | None
    opportunity_status_rec_i_ds: list[int] | None
    add_all_opportunity_statuses: bool | None
    remove_all_opportunity_statuses: bool | None
    opportunity_type_rec_i_ds: list[int] | None
    add_all_opportunity_types: bool | None
    remove_all_opportunity_types: bool | None
    restrict_view_by_opportunity_status_flag: bool | None
    restrict_view_by_opportunity_type_flag: bool | None
    acceptance_change_status_flag: bool | None
    acceptance_create_activity_flag: bool | None
    acceptance_opportunity_status: OpportunityStatusReferenceModel | None
    acceptance_send_email_flag: bool | None
    acceptance_email_from_first_name: str | None
    acceptance_email_from_last_name: str | None
    acceptance_email_subject: str | None
    acceptance_email_body: str | None
    acceptance_from_email: str | None
    acceptance_email_activity_type: ActivityTypeReferenceModel | None
    acceptance_email_assigned_by_member: MemberReferenceModel | None
    rejection_change_status_flag: bool | None
    rejection_create_activity_flag: bool | None
    rejection_opportunity_status: OpportunityStatusReferenceModel | None
    rejection_send_email_flag: bool | None
    rejection_email_from_first_name: str | None
    rejection_email_from_last_name: str | None
    rejection_from_email: str | None
    rejection_email_subject: str | None
    rejection_email_body: str | None
    rejection_email_activity_type: ActivityTypeReferenceModel | None
    rejection_email_assigned_by_member: MemberReferenceModel | None
    confirmation_send_email_flag: bool | None
    confirmation_email_use_default_company_email_address_flag: bool | None
    confirmation_email_from_first_name: str | None
    confirmation_email_from_last_name: str | None
    confirmation_from_email: str | None
    confirmation_email_subject: str | None
    confirmation_email_body: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True