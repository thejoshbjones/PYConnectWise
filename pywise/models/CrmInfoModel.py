from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.TeamRoleReferenceModel import TeamRoleReferenceModel
from pywise.models.TeamRoleReferenceModel import TeamRoleReferenceModel
from pywise.models.TeamRoleReferenceModel import TeamRoleReferenceModel

class CrmInfoModel(ConnectWiseModel):
    id: int | None
    account_manager_role: TeamRoleReferenceModel | None
    technical_contact_role: TeamRoleReferenceModel | None
    sales_rep_role: TeamRoleReferenceModel | None
    field1_caption: str | None
    field2_caption: str | None
    field3_caption: str | None
    field4_caption: str | None
    field5_caption: str | None
    field6_caption: str | None
    field7_caption: str | None
    field8_caption: str | None
    field9_caption: str | None
    field10_caption: str | None
    primary_rep_caption: str | None
    secondary_rep_caption: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True