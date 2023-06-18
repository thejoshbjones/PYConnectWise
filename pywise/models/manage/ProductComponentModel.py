from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ProductItemReferenceModel import ProductItemReferenceModel
from pywise.models.manage.ProductItemReferenceModel import ProductItemReferenceModel

class ProductComponentModel(ConnectWiseModel):
    id: int | None
    sequence_number: int | None
    quantity: float | None
    catalog_item: CatalogItemReferenceModel | None
    hide_price_flag: bool | None
    hide_item_identifier_flag: bool | None
    hide_description_flag: bool | None
    hide_quantity_flag: bool | None
    hide_extended_price_flag: bool | None
    vendor: CompanyReferenceModel | None
    parent_product_item: ProductItemReferenceModel | None
    product_item: ProductItemReferenceModel | None
    price: float | None
    cost: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True