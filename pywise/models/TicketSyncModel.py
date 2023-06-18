from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.IntegratorLoginReferenceModel import IntegratorLoginReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
class VendorType(str, Enum):
    Zenith = 'Zenith'

class TicketSyncModel(ConnectWiseModel):
    id: int | None
    name: str | None
    vendor_type: VendorType | None
    integrator_login: IntegratorLoginReferenceModel | None
    company: CompanyReferenceModel | None
    url: str | None
    user_name: str | None
    password: str | None
    psg: str | None
    problem_description_flag: bool | None
    internal_analysis_flag: bool | None
    resolution_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True