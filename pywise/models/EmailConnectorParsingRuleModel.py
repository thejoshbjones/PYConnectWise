from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.EmailConnectorParsingStyleReferenceModel import EmailConnectorParsingStyleReferenceModel
from pywise.models.EmailConnectorParsingVariableReferenceModel import EmailConnectorParsingVariableReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel

class EmailConnectorParsingRuleModel(ConnectWiseModel):
    id: int | None
    parsing_style: EmailConnectorParsingStyleReferenceModel | None
    priority: int | None
    parsing_variable: EmailConnectorParsingVariableReferenceModel | None
    search_term: str | None
    service_priority: PriorityReferenceModel | None
    service_status: ServiceStatusReferenceModel | None
    service_type: ServiceTypeReferenceModel | None
    service_sub_type: ServiceSubTypeReferenceModel | None
    service_item: ServiceItemReferenceModel | None
    service_board: BoardReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True