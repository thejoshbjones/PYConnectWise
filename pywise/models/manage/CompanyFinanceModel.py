from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.EmailTemplateReferenceModel import EmailTemplateReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class CompanyFinanceModel(ConnectWiseModel):
    id: int
    bill_override_flag: bool
    bill_sr_flag: bool
    bill_complete_sr_flag: bool
    bill_unapproved_sr_flag: bool
    bill_restrict_pm_flag: bool
    bill_complete_pm_flag: bool
    bill_unapproved_pm_flag: bool
    email_template: EmailTemplateReferenceModel
    company: CompanyReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True