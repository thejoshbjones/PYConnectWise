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
    id: int
    notify_type: NotifyTypeReferenceModel
    notify_who: NotificationRecipientReferenceModel
    specific_member_to: MemberReferenceModel
    email_recipient: str
    notify_from: NotificationRecipientReferenceModel
    specific_member_from: MemberReferenceModel
    email_from: str
    cc_contact: ContactReferenceModel
    bcc_contact: ContactReferenceModel
    subject: str
    notes: str
    activity_status: ActivityStatusReferenceModel
    activity_type: ActivityTypeReferenceModel
    attached_track: TrackReferenceModel
    days_to_execute: int
    board: BoardReferenceModel
    board_status: ServiceStatusReferenceModel
    service_type: ServiceTypeReferenceModel
    service_sub_type: ServiceSubTypeReferenceModel
    service_item: ServiceItemReferenceModel
    group: GroupReferenceModel
    service_template: ServiceTemplateReferenceModel
    invoice_min_days: int
    automate_script: AutomateScriptReferenceModel
    script_success_status: ServiceStatusReferenceModel
    script_fail_status: ServiceStatusReferenceModel
    detail_notes_flag: bool
    internal_notes_flag: bool
    audit_notes_flag: bool
    service_priority: PriorityReferenceModel
    update_owner_flag: bool
    sales_order_status: OrderStatusReferenceModel
    project_status: ProjectStatusReferenceModel
    company_status: CompanyStatusReferenceModel
    attachments: list[int]
    service_survey: ServiceSurveyReferenceModel
    specific_team_to: GenericBoardTeamReferenceModel
    attach_configurations_for: AttachConfigurationsFor
    configuration_type: ConfigurationTypeReferenceModel
    configuration_status: ConfigurationStatusReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True