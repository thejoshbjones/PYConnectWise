from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.GLExportExpenseOffsetModel import GLExportExpenseOffsetModel

class GLExportExpenseModel(ConnectWiseModel):
    id: int | None
    document_date: str | None
    document_type: str | None
    ap_account_number: str | None
    ap_class: str | None
    account_number: str | None
    gl_class: str | None
    gl_type_id: str | None
    memo: str | None
    description: str | None
    period_start_date: str | None
    period_end_date: str | None
    member: MemberReferenceModel | None
    vendor_number: str | None
    company: CompanyReferenceModel | None
    company_account_number: str | None
    project: ProjectReferenceModel | None
    currency: CurrencyReferenceModel | None
    total: float | None
    offset: GLExportExpenseOffsetModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True