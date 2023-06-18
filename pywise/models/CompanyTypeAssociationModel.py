from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel

class CompanyTypeAssociationModel(ConnectWiseModel):
    id: int | None
    type: CompanyTypeReferenceModel | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True