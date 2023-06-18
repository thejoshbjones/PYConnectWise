from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.BoardReferenceModel import BoardReferenceModel

class KnowledgeBaseArticleModel(ConnectWiseModel):
    id: int | None
    title: str | None
    issue: str | None
    resolution: str | None
    location_id: int | None
    business_unit_id: int | None
    board: BoardReferenceModel | None
    category_id: int | None
    sub_category_id: int | None
    date_created: str | None
    created_by: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True