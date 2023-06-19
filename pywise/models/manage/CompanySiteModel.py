from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.StateReferenceModel import StateReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.EntityTypeReferenceModel import EntityTypeReferenceModel
from pywise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class CompanySiteModel(ConnectWiseModel):
    id: int
    name: str
    address_line1: str
    address_line2: str
    city: str
    state_reference: StateReferenceModel
    zip: str
    country: CountryReferenceModel
    address_format: str
    phone_number: str
    fax_number: str
    tax_code: TaxCodeReferenceModel
    entity_type: EntityTypeReferenceModel
    expense_reimbursement: float
    primary_address_flag: bool
    default_shipping_flag: bool
    default_billing_flag: bool
    default_mailing_flag: bool
    inactive_flag: bool
    bill_separate_flag: bool
    mobile_guid: str
    calendar: CalendarReferenceModel
    time_zone: TimeZoneSetupReferenceModel
    company: CompanyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True