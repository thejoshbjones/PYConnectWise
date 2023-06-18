from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pywise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel

class PricingDetailModel(ConnectWiseModel):
    id: int | None
    product: CatalogItemReferenceModel | None
    category: ProductCategoryReferenceModel | None
    sub_category: ProductSubCategoryReferenceModel | None
    start_date: str | None
    end_date: str | None
    no_end_date: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True