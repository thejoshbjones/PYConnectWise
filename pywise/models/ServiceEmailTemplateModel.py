from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.ServiceSurveyReferenceModel import ServiceSurveyReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
class ServiceEmailTemplateModelType(str, Enum):
    Any = 'Any'
    Closed = 'Closed'
    Invoice = 'Invoice'
    New = 'New'
    SalesOrder = 'SalesOrder'
    PurchaseOrder = 'PurchaseOrder'
    RMA = 'RMA'
    Specific = 'Specific'

class ServiceEmailTemplateModel(ConnectWiseModel):
    id: int | None
    type: ServiceEmailTemplateModelType | None
    service_survey: ServiceSurveyReferenceModel | None
    service_board: BoardReferenceModel | None
    use_sender_flag: bool | None
    first_name: str | None
    last_name: str | None
    email_address: str | None
    subject: str | None
    body: str | None
    copy_sender_flag: bool | None
    tasks_flag: bool | None
    resource_records_flag: bool | None
    external_contact_notifications: bool | None
    internal_contact_notifications: bool | None
    service_status: ServiceStatusReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True