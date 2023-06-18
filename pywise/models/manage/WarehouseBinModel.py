from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel

class WarehouseBinModel(ConnectWiseModel):
    id: int | None
    name: str | None
    warehouse: WarehouseReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    min_quantity: float | None
    max_quantity: float | None
    overflow_bin: WarehouseBinReferenceModel | None
    manager: MemberReferenceModel | None
    length: float | None
    width: float | None
    height: float | None
    weight: float | None
    default_flag: bool | None
    inactive_flag: bool | None
    quantity_on_hand: int | None
    company: CompanyReferenceModel | None
    transfer_bin: WarehouseBinReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True