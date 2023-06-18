from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel

class ManagementReportNotificationModel(ConnectWiseModel):
    id: int | None
    notify_who: NotificationRecipientReferenceModel | None
    member: MemberReferenceModel | None
    email: str | None
    global_flag: bool | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True