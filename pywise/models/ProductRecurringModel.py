from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class CycleType(str, Enum):
    ContractYear = 'ContractYear'
    CalendarYear = 'CalendarYear'

class ProductRecurringModel(ConnectWiseModel):
    recurring_revenue: float | None
    recurring_cost: float | None
    start_date: str | None
    end_date: str | None
    bill_cycle_id: int | None
    cycles: int | None
    cycle_type: CycleType | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True