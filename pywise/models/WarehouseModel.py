from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class WarehouseModel(ConnectWiseModel):
    id: int | None
    name: str | None
    company: CompanyReferenceModel | None
    location: SystemLocationReferenceModel | None
    contact: ContactReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    manager: MemberReferenceModel | None
    site: SiteReferenceModel | None
    location_xref: str | None
    location_default_flag: bool | None
    overall_default_flag: bool | None
    inactive_flag: bool | None
    locked_flag: bool | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True