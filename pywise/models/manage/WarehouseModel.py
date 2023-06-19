from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class WarehouseModel(ConnectWiseModel):
    id: int
    name: str
    company: CompanyReferenceModel
    location: SystemLocationReferenceModel
    contact: ContactReferenceModel
    department: SystemDepartmentReferenceModel
    manager: MemberReferenceModel
    site: SiteReferenceModel
    location_xref: str
    location_default_flag: bool
    overall_default_flag: bool
    inactive_flag: bool
    locked_flag: bool
    currency: CurrencyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True