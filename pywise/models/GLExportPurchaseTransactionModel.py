from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.GLExportPurchaseTransactionTaxLevelModel import GLExportPurchaseTransactionTaxLevelModel
from pywise.models.GLExportPurchaseTransactionDetailModel import GLExportPurchaseTransactionDetailModel
from pywise.models.GLExportPurchaseTransactionDetailTaxModel import GLExportPurchaseTransactionDetailTaxModel

class GLExportPurchaseTransactionModel(ConnectWiseModel):
    id: str | None
    document_date: str | None
    document_number: str | None
    description: str | None
    memo: str | None
    ap_account_number: str | None
    purchase_date: str | None
    company: CompanyReferenceModel | None
    company_type: CompanyTypeReferenceModel | None
    contact: ContactReferenceModel | None
    site: SiteReferenceModel | None
    purchase_class: str | None
    freight_amount: float | None
    freight_packing_slip: str | None
    packing_slip: str | None
    dropship_flag: bool | None
    currency: CurrencyReferenceModel | None
    total: float | None
    billing_terms: BillingTermsReferenceModel | None
    billing_terms_xref: str | None
    due_days: int | None
    vendor_number: str | None
    vendor_account_number: str | None
    vendor_invoice_date: str | None
    vendor_invoice_number: str | None
    tax_agency_xref: str | None
    state_tax_xref: str | None
    county_tax_xref: str | None
    city_tax_xref: str | None
    ship_to_company: CompanyReferenceModel | None
    ship_to_company_account_number: str | None
    ship_to_company_type: CompanyTypeReferenceModel | None
    ship_to_contact: ContactReferenceModel | None
    ship_to_site: SiteReferenceModel | None
    ship_to_tax_group: str | None
    tax_code: TaxCodeReferenceModel | None
    tax_group_rate: float | None
    use_avalara_tax_flag: bool | None
    purchase_header_tax_group: str | None
    purchase_header_taxable_flag: bool | None
    purchase_header_freight_taxable_flag: bool | None
    tax_levels: list[GLExportPurchaseTransactionTaxLevelModel] | None
    purchase_detail: list[GLExportPurchaseTransactionDetailModel] | None
    purchase_detail_tax: list[GLExportPurchaseTransactionDetailTaxModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True