from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CatalogItemReferenceModel import CatalogItemReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel

class CatalogPricingModel(ConnectWiseModel):
    catalog_item: CatalogItemReferenceModel | None
    company: CompanyReferenceModel | None
    location: SystemLocationReferenceModel | None
    quantity: int | None
    date: str | None
    price: float | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True