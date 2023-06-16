from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pywise.models.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel

class CompanyPickerItemModel(ConnectWiseModel):
    id: int | None
    member: MemberReferenceModel | None
    company: CompanyReferenceModel | None
    company_status: CompanyStatusReferenceModel | None
    company_type: CompanyTypeReferenceModel | None
    company_site: SiteReferenceModel | None
    company_location: SystemLocationReferenceModel | None
    company_country: CountryReferenceModel | None
    vendor_picker_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True