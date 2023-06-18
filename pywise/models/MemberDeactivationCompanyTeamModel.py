from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel

class MemberDeactivationCompanyTeamModel(ConnectWiseModel):
    count: int | None
    id: int | None
    name: str | None
    re_assign_to_member: MemberReferenceModel | None
    re_assign_to_contact: ContactReferenceModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True