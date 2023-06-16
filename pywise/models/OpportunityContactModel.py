from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.OpportunitySalesRoleReferenceModel import OpportunitySalesRoleReferenceModel

class OpportunityContactModel(ConnectWiseModel):
    id: int | None
    contact: ContactReferenceModel | None
    company: CompanyReferenceModel | None
    role: OpportunitySalesRoleReferenceModel | None
    notes: str | None
    referral_flag: bool | None
    opportunity_id: int | None
    phone_number: str | None
    email_address: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True