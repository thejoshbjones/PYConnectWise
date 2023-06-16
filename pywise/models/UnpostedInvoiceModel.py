from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from enum import Enum
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
class InvoiceType(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'

class UnpostedInvoiceModel(ConnectWiseModel):
    id: int | None
    billing_log_id: int | None
    location_id: int | None
    department_id: int | None
    company: CompanyReferenceModel | None
    account_number: str | None
    bill_to_company: CompanyReferenceModel | None
    bill_to_site: SiteReferenceModel | None
    ship_to_company: CompanyReferenceModel | None
    ship_to_site: SiteReferenceModel | None
    invoice_number: str | None
    invoice_date: str | None
    invoice_type: InvoiceType | None
    description: str | None
    billing_terms: BillingTermsReferenceModel | None
    due_days: str | None
    due_date: str | None
    currency: CurrencyReferenceModel | None
    sub_total: float | None
    total: float | None
    invoice_taxable_flag: bool | None
    tax_code: TaxCodeReferenceModel | None
    avalara_tax_flag: bool | None
    item_taxable_flag: bool | None
    sales_tax_amount: float | None
    state_tax_flag: bool | None
    state_tax_xref: str | None
    state_tax_amount: float | None
    county_tax_flag: bool | None
    county_tax_xref: str | None
    county_tax_amount: float | None
    city_tax_flag: bool | None
    city_tax_xref: str | None
    city_tax_amount: float | None
    country_tax_flag: bool | None
    country_tax_xref: str | None
    country_tax_amount: float | None
    composite_tax_flag: bool | None
    composite_tax_xref: str | None
    composite_tax_amount: float | None
    level_six_tax_flag: bool | None
    level_six_tax_xref: str | None
    level_six_tax_amount: float | None
    created_by: str | None
    date_closed: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True