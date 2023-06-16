from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.EmailConnectorParsingTypeReferenceModel import EmailConnectorParsingTypeReferenceModel

class EmailConnectorParsingStyleModel(ConnectWiseModel):
    id: int | None
    parsing_type: EmailConnectorParsingTypeReferenceModel | None
    parse_rule: str | None
    priority: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True