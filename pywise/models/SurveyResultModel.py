from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SurveyResultDetailModel import SurveyResultDetailModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel

class SurveyResultModel(ConnectWiseModel):
    id: int | None
    ticket_id: int | None
    email_address: str | None
    footer_response: str | None
    contact_me_flag: bool | None
    contact: ContactReferenceModel | None
    results: list[SurveyResultDetailModel] | None
    total_points: int | None
    company: CompanyReferenceModel | None
    survey_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True