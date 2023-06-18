from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.GLExportCustomerTaxLevelModel import GLExportCustomerTaxLevelModel

class GLExportCustomerModel(ConnectWiseModel):
    company: CompanyReferenceModel | None
    company_type: CompanyTypeReferenceModel | None
    contact: ContactReferenceModel | None
    site: SiteReferenceModel | None
    account_number: str | None
    billing_terms: BillingTermsReferenceModel | None
    billing_terms_xref: str | None
    due_days: int | None
    taxable: bool | None
    tax_code: TaxCodeReferenceModel | None
    currency: CurrencyReferenceModel | None
    state_tax_xref: str | None
    county_tax_xref: str | None
    city_tax_xref: str | None
    country_tax_xref: str | None
    composite_tax_xref: str | None
    state_tax_rate: float | None
    county_tax_rate: float | None
    city_tax_rate: float | None
    country_tax_rate: float | None
    composite_tax_rate: float | None
    tax_group_rate: float | None
    tax_agency_xref: str | None
    state_tax_agency_xref: str | None
    county_tax_agency_xref: str | None
    city_tax_agency_xref: str | None
    country_tax_agency_xref: str | None
    composite_tax_agency_xref: str | None
    tax_levels: list[GLExportCustomerTaxLevelModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True