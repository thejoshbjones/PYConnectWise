from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.MarketDescriptionReferenceModel import MarketDescriptionReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SicCodeReferenceModel import SicCodeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.OwnershipTypeReferenceModel import OwnershipTypeReferenceModel
from pywise.models.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.PricingScheduleReferenceModel import PricingScheduleReferenceModel
from pywise.models.EntityTypeReferenceModel import EntityTypeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.BillingDeliveryReferenceModel import BillingDeliveryReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel

class CompanyModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    name: str | None
    status: CompanyStatusReferenceModel | None
    address_line1: str | None
    address_line2: str | None
    city: str | None
    state: str | None
    zip: str | None
    country: CountryReferenceModel | None
    phone_number: str | None
    fax_number: str | None
    website: str | None
    territory: SystemLocationReferenceModel | None
    market: MarketDescriptionReferenceModel | None
    account_number: str | None
    default_contact: ContactReferenceModel | None
    date_acquired: str | None
    sic_code: SicCodeReferenceModel | None
    parent_company: CompanyReferenceModel | None
    annual_revenue: float | None
    number_of_employees: int | None
    year_established: int | None
    revenue_year: int | None
    ownership_type: OwnershipTypeReferenceModel | None
    time_zone_setup: TimeZoneSetupReferenceModel | None
    lead_source: str | None
    lead_flag: bool | None
    unsubscribe_flag: bool | None
    calendar: CalendarReferenceModel | None
    user_defined_field1: str | None
    user_defined_field2: str | None
    user_defined_field3: str | None
    user_defined_field4: str | None
    user_defined_field5: str | None
    user_defined_field6: str | None
    user_defined_field7: str | None
    user_defined_field8: str | None
    user_defined_field9: str | None
    user_defined_field10: str | None
    vendor_identifier: str | None
    tax_identifier: str | None
    tax_code: TaxCodeReferenceModel | None
    billing_terms: BillingTermsReferenceModel | None
    invoice_template: InvoiceTemplateReferenceModel | None
    pricing_schedule: PricingScheduleReferenceModel | None
    company_entity_type: EntityTypeReferenceModel | None
    bill_to_company: CompanyReferenceModel | None
    billing_site: SiteReferenceModel | None
    billing_contact: ContactReferenceModel | None
    invoice_delivery_method: BillingDeliveryReferenceModel | None
    invoice_to_email_address: str | None
    invoice_c_c_email_address: str | None
    deleted_flag: bool | None
    date_deleted: str | None
    deleted_by: str | None
    mobile_guid: str | None
    facebook_url: str | None
    twitter_url: str | None
    linked_in_url: str | None
    currency: CurrencyReferenceModel | None
    territory_manager: MemberReferenceModel | None
    reseller_identifier: str | None
    is_vendor_flag: bool | None
    types: list[CompanyTypeReferenceModel] | None
    site: SiteReferenceModel | None
    integrator_tags: list[str] | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True