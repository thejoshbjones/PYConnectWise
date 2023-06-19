from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.ServiceTemplateReferenceModel import ServiceTemplateReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.manage.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pywise.models.manage.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pywise.models.manage.TrackReferenceModel import TrackReferenceModel
from pywise.models.manage.TrackReferenceModel import TrackReferenceModel
from pywise.models.manage.GroupReferenceModel import GroupReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
class NotifyType(str, Enum):
    CreateActivity = 'CreateActivity'
    SendEmail = 'SendEmail'
    AddToGroup = 'AddToGroup'
    AttachTrack = 'AttachTrack'
    ChangeCompanyStatus = 'ChangeCompanyStatus'
    CreateServiceTicket = 'CreateServiceTicket'

class TrackActionModel(ConnectWiseModel):
    id: int
    notify_type: NotifyType
    service_template: ServiceTemplateReferenceModel
    specific_member_to: MemberReferenceModel
    email_recipient: str
    specific_member_from: MemberReferenceModel
    email_from: str
    subject: str
    notes: str
    activity_type: ActivityTypeReferenceModel
    activity_status: ActivityStatusReferenceModel
    company_status: CompanyStatusReferenceModel
    track: TrackReferenceModel
    attached_track: TrackReferenceModel
    group: GroupReferenceModel
    cc_contact: ContactReferenceModel
    bcc_contact: ContactReferenceModel
    days_to_execute: int
    notify_who: NotificationRecipientReferenceModel
    notify_from: NotificationRecipientReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True