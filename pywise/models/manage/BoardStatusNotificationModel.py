from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

class BoardStatusNotificationModel(ConnectWiseModel):
    id: int
    notify_who: NotificationRecipientReferenceModel
    status: ServiceStatusReferenceModel
    member: MemberReferenceModel
    email: str
    workflow_step: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True