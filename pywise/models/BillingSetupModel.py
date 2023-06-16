from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.StateReferenceModel import StateReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pywise.models.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from enum import Enum
from pywise.models.EmailTemplateReferenceModel import EmailTemplateReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
class PrefixSuffixFlag(str, Enum):
    Prefix = 'Prefix'
    Suffix = 'Suffix'

class BillingSetupModel(ConnectWiseModel):
    id: int | None
    remit_name: str | None
    location: SystemLocationReferenceModel | None
    address_one: str | None
    address_two: str | None
    city: str | None
    state: StateReferenceModel | None
    zip: str | None
    country: CountryReferenceModel | None
    phone: str | None
    invoice_title: str | None
    payable_name: str | None
    topcomment: str | None
    invoice_footer: str | None
    quote_footer: str | None
    overall_invoice_default: InvoiceTemplateReferenceModel | None
    standard_invoice_actual: InvoiceTemplateReferenceModel | None
    standard_invoice_fixed: InvoiceTemplateReferenceModel | None
    progress_invoice: InvoiceTemplateReferenceModel | None
    agreement_invoice: InvoiceTemplateReferenceModel | None
    credit_memo_invoice: InvoiceTemplateReferenceModel | None
    down_payment_invoice: InvoiceTemplateReferenceModel | None
    misc_invoice: InvoiceTemplateReferenceModel | None
    sales_order_invoice: InvoiceTemplateReferenceModel | None
    exclude_do_not_bill_time_flag: bool | None
    exclude_do_not_bill_expense_flag: bool | None
    exclude_do_not_bill_product_flag: bool | None
    prefix_suffix_flag: PrefixSuffixFlag | None
    prefix_suffix_text: str | None
    charge_adj_to_firm_flag: bool | None
    no_watermark_flag: bool | None
    display_tax_flag: bool | None
    allow_restricted_dept_on_routing_flag: bool | None
    bill_ticket_separately_flag: bool | None
    bill_ticket_complete_flag: bool | None
    bill_ticket_unapproved_flag: bool | None
    bill_project_complete_flag: bool | None
    bill_project_unapproved_flag: bool | None
    progress_time_flag: bool | None
    restrict_project_downpayment_flag: bool | None
    bill_sales_order_complete_flag: bool | None
    bill_product_after_ship_flag: bool | None
    restrict_downpayment_flag: bool | None
    copy_non_service_products_flag: bool | None
    copy_service_products_flag: bool | None
    copy_agreement_products_flag: bool | None
    print_logo_flag: bool | None
    read_receipt_flag: bool | None
    delivery_receipt_flag: bool | None
    disable_routing_email_flag: bool | None
    email_template: EmailTemplateReferenceModel | None
    localized_country: CountryReferenceModel | None
    business_number: str | None
    currency: CurrencyReferenceModel | None
    custom_label: str | None
    custom_text: str | None
    company_code: str | None
    exclude_avalara_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True