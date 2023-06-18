from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class CompanyCustomNoteModel(ConnectWiseModel):
    id: int | None
    custom_note: str | None
    status: CompanyStatusReferenceModel | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True