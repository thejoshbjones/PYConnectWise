from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ClassificationReferenceModel import ClassificationReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class GLExportExpenseBillDetailModel(ConnectWiseModel):
    id: list[int] | None
    document_date: str | None
    gl_type_id: str | None
    memo: str | None
    company: CompanyReferenceModel | None
    account_number: str | None
    expense_class: ClassificationReferenceModel | None
    currency: CurrencyReferenceModel | None
    total: float | None
    billable: bool | None
    reimbursable: bool | None
    company_advance: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True