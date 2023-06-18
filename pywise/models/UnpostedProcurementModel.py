from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.PurchaseOrderReferenceModel import PurchaseOrderReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
class ProcurementType(str, Enum):
    Purchase = 'Purchase'
    Adjustment = 'Adjustment'
    Transfer = 'Transfer'

class UnpostedProcurementModel(ConnectWiseModel):
    id: int | None
    description: str | None
    unposted_product_id: str | None
    location_id: int | None
    department_id: int | None
    procurement_type: ProcurementType | None
    purchase_order: PurchaseOrderReferenceModel | None
    purchase_date: str | None
    tracking_number: str | None
    billing_terms: BillingTermsReferenceModel | None
    currency: CurrencyReferenceModel | None
    total: float | None
    tax_code: TaxCodeReferenceModel | None
    avalara_tax_flag: bool | None
    item_taxable_flag: bool | None
    purchase_order_taxable_flag: bool | None
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
    tax_total: float | None
    customer: CompanyReferenceModel | None
    vendor: CompanyReferenceModel | None
    vendor_account_number: str | None
    vendor_invoice_number: str | None
    vendor_invoice_date: str | None
    tax_freight_flag: bool | None
    freight_tax_total: float | None
    freight_cost: float | None
    date_closed: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True