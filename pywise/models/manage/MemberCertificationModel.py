from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CertificationReferenceModel import CertificationReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class MemberCertificationModel(ConnectWiseModel):
    id: int
    certification: CertificationReferenceModel
    percent_complete: int
    date_received: str
    date_expires: str
    certification_number: str
    notes: str
    member: MemberReferenceModel
    company: CompanyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True