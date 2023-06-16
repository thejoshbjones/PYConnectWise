from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class PricingScheduleModel(ConnectWiseModel):
    id: int | None
    name: str | None
    inactive_flag: bool | None
    default_flag: bool | None
    currency: CurrencyReferenceModel | None
    companies: list[int] | None
    set_all_companies_flag: bool | None
    remove_all_companies_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True