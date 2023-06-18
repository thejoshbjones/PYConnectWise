from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ChargeCodeReferenceModel import ChargeCodeReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel

class ScheduleTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    identifier: str | None
    charge_code: ChargeCodeReferenceModel | None
    where: ServiceLocationReferenceModel | None
    system_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True