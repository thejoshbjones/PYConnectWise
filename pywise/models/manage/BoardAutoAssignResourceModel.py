from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel

class BoardAutoAssignResourceModel(ConnectWiseModel):
    id: int | None
    notify_who: NotificationRecipientReferenceModel | None
    member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True