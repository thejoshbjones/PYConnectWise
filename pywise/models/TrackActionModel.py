from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.ServiceTemplateReferenceModel import ServiceTemplateReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pywise.models.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pywise.models.TrackReferenceModel import TrackReferenceModel
from pywise.models.TrackReferenceModel import TrackReferenceModel
from pywise.models.GroupReferenceModel import GroupReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
class NotifyType(str, Enum):
    CreateActivity = 'CreateActivity'
    SendEmail = 'SendEmail'
    AddToGroup = 'AddToGroup'
    AttachTrack = 'AttachTrack'
    ChangeCompanyStatus = 'ChangeCompanyStatus'
    CreateServiceTicket = 'CreateServiceTicket'

class TrackActionModel(ConnectWiseModel):
    id: int | None
    notify_type: NotifyType | None
    service_template: ServiceTemplateReferenceModel | None
    specific_member_to: MemberReferenceModel | None
    email_recipient: str | None
    specific_member_from: MemberReferenceModel | None
    email_from: str | None
    subject: str | None
    notes: str | None
    activity_type: ActivityTypeReferenceModel | None
    activity_status: ActivityStatusReferenceModel | None
    company_status: CompanyStatusReferenceModel | None
    track: TrackReferenceModel | None
    attached_track: TrackReferenceModel | None
    group: GroupReferenceModel | None
    cc_contact: ContactReferenceModel | None
    bcc_contact: ContactReferenceModel | None
    days_to_execute: int | None
    notify_who: NotificationRecipientReferenceModel | None
    notify_from: NotificationRecipientReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True