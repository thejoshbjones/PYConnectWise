from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ServiceSurveyReferenceModel import ServiceSurveyReferenceModel
from pywise.models.manage.BillingStatusReferenceModel import BillingStatusReferenceModel

class InvoiceEmailTemplateModel(ConnectWiseModel):
    id: int | None
    name: str | None
    service_survey: ServiceSurveyReferenceModel | None
    use_sender_flag: bool | None
    first_name: str | None
    last_name: str | None
    email_address: str | None
    subject: str | None
    body: str | None
    copy_sender_flag: bool | None
    invoice_status: BillingStatusReferenceModel | None
    attach_invoice_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True