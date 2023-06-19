from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel

class CatalogPricingModel(ConnectWiseModel):
    catalog_item: CatalogItemReferenceModel
    company: CompanyReferenceModel
    location: SystemLocationReferenceModel
    quantity: int
    date: str
    price: float

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True