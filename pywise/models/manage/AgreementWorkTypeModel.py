from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from enum import Enum
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
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

class AgreementWorkTypeModel(ConnectWiseModel):
    id: int | None
    work_type: WorkTypeReferenceModel | None
    location_id: int | None
    rate_type: RateType | None
    bill_time: BillTime | None
    rate: float | None
    hours_max: float | None
    hours_min: float | None
    round_bill_hours: float | None
    overage_rate: float | None
    overage_rate_type: OverageRateType | None
    agreement_limit: float | None
    site: SiteReferenceModel | None
    effective_date: str | None
    ending_date: str | None
    agreement_id: int | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True