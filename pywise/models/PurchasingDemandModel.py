from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ProductDemandModel import ProductDemandModel
from pywise.models.PurchaseOrderModel import PurchaseOrderModel

class PurchasingDemandModel(ConnectWiseModel):
    warehouse: WarehouseReferenceModel | None
    vendor: CompanyReferenceModel | None
    products: list[ProductDemandModel] | None
    purchase_order: PurchaseOrderModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True