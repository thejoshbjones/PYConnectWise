from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.EmailTemplateReferenceModel import EmailTemplateReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class CompanyFinanceModel(ConnectWiseModel):
    id: int | None
    bill_override_flag: bool | None
    bill_sr_flag: bool | None
    bill_complete_sr_flag: bool | None
    bill_unapproved_sr_flag: bool | None
    bill_restrict_pm_flag: bool | None
    bill_complete_pm_flag: bool | None
    bill_unapproved_pm_flag: bool | None
    email_template: EmailTemplateReferenceModel | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True