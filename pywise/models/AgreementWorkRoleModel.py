from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel
from enum import Enum
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'

class AgreementWorkRoleModel(ConnectWiseModel):
    id: int | None
    work_role: WorkRoleReferenceModel | None
    location_id: int | None
    rate_type: RateType | None
    rate: float | None
    limit_to: float | None
    effective_date: str | None
    ending_date: str | None
    agreement_id: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True