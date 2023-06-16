from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.OpportunityProbabilityReferenceModel import OpportunityProbabilityReferenceModel

class OpportunityStageModel(ConnectWiseModel):
    id: int | None
    name: str | None
    probability: OpportunityProbabilityReferenceModel | None
    color: str | None
    sequence_number: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True