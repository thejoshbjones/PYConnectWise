from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class NotificationType(str, Enum):
    Email = 'Email'
    Push = 'Push'
class NotificationTrigger(str, Enum):
    ActivityStatusReq = 'ActivityStatusReq'
    CustomerUpdated = 'CustomerUpdated'
    ExpenseReport = 'ExpenseReport'
    TicketStatusChange = 'TicketStatusChange'
    TicketStatusRequest = 'TicketStatusRequest'
    TimeNagApprover = 'TimeNagApprover'
    TimeNagMember = 'TimeNagMember'
    TimeSheet = 'TimeSheet'
    WorkflowRules = 'WorkflowRules'

class MemberNotificationSettingModel(ConnectWiseModel):
    id: int | None
    notification_type: NotificationType | None
    notification_trigger: NotificationTrigger | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True