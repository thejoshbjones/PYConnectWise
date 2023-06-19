from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel

class KnowledgeBaseArticleModel(ConnectWiseModel):
    id: int
    title: str
    issue: str
    resolution: str
    location_id: int
    business_unit_id: int
    board: BoardReferenceModel
    category_id: int
    sub_category_id: int
    date_created: str
    created_by: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True