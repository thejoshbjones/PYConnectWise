from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ProductCategoryReferenceModel import ProductCategoryReferenceModel

class SubCategoryModel(ConnectWiseModel):
    id: int | None
    name: str | None
    inactive_flag: bool | None
    integration_xref: str | None
    default_flag: bool | None
    category: ProductCategoryReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True