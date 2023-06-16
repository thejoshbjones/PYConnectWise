from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CertificationReferenceModel import CertificationReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel

class MemberCertificationModel(ConnectWiseModel):
    id: int | None
    certification: CertificationReferenceModel | None
    percent_complete: int | None
    date_received: str | None
    date_expires: str | None
    certification_number: str | None
    notes: str | None
    member: MemberReferenceModel | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True