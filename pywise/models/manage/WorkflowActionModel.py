from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.NotifyTypeReferenceModel import NotifyTypeReferenceModel
from pywise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pywise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.manage.TrackReferenceModel import TrackReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.manage.GroupReferenceModel import GroupReferenceModel
from pywise.models.manage.ServiceTemplateReferenceModel import ServiceTemplateReferenceModel
from pywise.models.manage.AutomateScriptReferenceModel import AutomateScriptReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.OrderStatusReferenceModel import OrderStatusReferenceModel
from pywise.models.manage.ProjectStatusReferenceModel import ProjectStatusReferenceModel
from pywise.models.manage.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pywise.models.manage.ServiceSurveyReferenceModel import ServiceSurveyReferenceModel
from pywise.models.manage.GenericBoardTeamReferenceModel import GenericBoardTeamReferenceModel
from enum import Enum
from pywise.models.manage.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel
from pywise.models.manage.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
class AttachConfigurationsFor(str, Enum):
    Company = 'Company'
    Contact = 'Contact'

class WorkflowActionModel(ConnectWiseModel):
    id: int | None
    notify_type: NotifyTypeReferenceModel | None
    notify_who: NotificationRecipientReferenceModel | None
    specific_member_to: MemberReferenceModel | None
    email_recipient: str | None
    notify_from: NotificationRecipientReferenceModel | None
    specific_member_from: MemberReferenceModel | None
    email_from: str | None
    cc_contact: ContactReferenceModel | None
    bcc_contact: ContactReferenceModel | None
    subject: str | None
    notes: str | None
    activity_status: ActivityStatusReferenceModel | None
    activity_type: ActivityTypeReferenceModel | None
    attached_track: TrackReferenceModel | None
    days_to_execute: int | None
    board: BoardReferenceModel | None
    board_status: ServiceStatusReferenceModel | None
    service_type: ServiceTypeReferenceModel | None
    service_sub_type: ServiceSubTypeReferenceModel | None
    service_item: ServiceItemReferenceModel | None
    group: GroupReferenceModel | None
    service_template: ServiceTemplateReferenceModel | None
    invoice_min_days: int | None
    automate_script: AutomateScriptReferenceModel | None
    script_success_status: ServiceStatusReferenceModel | None
    script_fail_status: ServiceStatusReferenceModel | None
    detail_notes_flag: bool | None
    internal_notes_flag: bool | None
    audit_notes_flag: bool | None
    service_priority: PriorityReferenceModel | None
    update_owner_flag: bool | None
    sales_order_status: OrderStatusReferenceModel | None
    project_status: ProjectStatusReferenceModel | None
    company_status: CompanyStatusReferenceModel | None
    attachments: list[int] | None
    service_survey: ServiceSurveyReferenceModel | None
    specific_team_to: GenericBoardTeamReferenceModel | None
    attach_configurations_for: AttachConfigurationsFor | None
    configuration_type: ConfigurationTypeReferenceModel | None
    configuration_status: ConfigurationStatusReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True