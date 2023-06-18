from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel

class AgreementSiteModel(ConnectWiseModel):
    id: int | None
    company: CompanyReferenceModel | None
    site: SiteReferenceModel | None
    agreement_id: int | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True