from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from enum import Enum
from pywise.models.ServiceEmailTemplateReferenceModel import ServiceEmailTemplateReferenceModel
from pywise.models.StatusIndicatorReferenceModel import StatusIndicatorReferenceModel
class EscalationStatus(str, Enum):
    NotResponded = 'NotResponded'
    Responded = 'Responded'
    ResolutionPlan = 'ResolutionPlan'
    Resolved = 'Resolved'
    NoEscalation = 'NoEscalation'

class BoardStatusModel(ConnectWiseModel):
    id: int | None
    name: str | None
    board: BoardReferenceModel | None
    sort_order: int | None
    display_on_board: bool | None
    inactive: bool | None
    closed_status: bool | None
    time_entry_not_allowed: bool | None
    default_flag: bool | None
    escalation_status: EscalationStatus | None
    customer_portal_description: str | None
    customer_portal_flag: bool | None
    email_template: ServiceEmailTemplateReferenceModel | None
    status_indicator: StatusIndicatorReferenceModel | None
    custom_status_indicator_name: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True