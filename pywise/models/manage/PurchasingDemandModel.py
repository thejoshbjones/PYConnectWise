from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ProductDemandModel import ProductDemandModel
from pywise.models.manage.PurchaseOrderModel import PurchaseOrderModel

class PurchasingDemandModel(ConnectWiseModel):
    warehouse: WarehouseReferenceModel
    vendor: CompanyReferenceModel
    products: list[ProductDemandModel]
    purchase_order: PurchaseOrderModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True