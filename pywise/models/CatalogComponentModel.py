from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.CatalogItemReferenceModel import CatalogItemReferenceModel

class CatalogComponentModel(ConnectWiseModel):
    id: int | None
    sequence_number: int | None
    quantity: float | None
    catalog_item: CatalogItemReferenceModel | None
    hide_price_flag: bool | None
    hide_item_identifier_flag: bool | None
    hide_description_flag: bool | None
    hide_quantity_flag: bool | None
    hide_extended_price_flag: bool | None
    parent_catalog_item: CatalogItemReferenceModel | None
    price: float | None
    cost: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True