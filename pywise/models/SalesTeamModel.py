from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel

class SalesTeamModel(ConnectWiseModel):
    id: int | None
    sales_team_identifier: str | None
    sales_team_description: str | None
    sales_team_location: SystemLocationReferenceModel | None
    inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True