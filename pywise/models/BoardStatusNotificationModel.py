from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel

class BoardStatusNotificationModel(ConnectWiseModel):
    id: int | None
    notify_who: NotificationRecipientReferenceModel | None
    status: ServiceStatusReferenceModel | None
    member: MemberReferenceModel | None
    email: str | None
    workflow_step: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True