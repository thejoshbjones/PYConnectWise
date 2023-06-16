from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.WorkTypeReferenceModel import WorkTypeReferenceModel
from enum import Enum
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class OverageRateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'

class AgreementTypeWorkTypeModel(ConnectWiseModel):
    id: int | None
    type: AgreementTypeReferenceModel | None
    work_type: WorkTypeReferenceModel | None
    effective_date: str | None
    ending_date: str | None
    rate: float | None
    rate_type: RateType | None
    bill_time: BillTime | None
    hours_min: float | None
    hours_max: float | None
    round_bill_hours: float | None
    overage_rate: float | None
    overage_rate_type: OverageRateType | None
    limit_to: float | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True