from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.BillingStatusReferenceModel import BillingStatusReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.InvoiceTemplateDetailReferenceModel import InvoiceTemplateDetailReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.BillingSetupReferenceModel import BillingSetupReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.manage.SalesOrderReferenceModel import SalesOrderReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class InvoiceModelType(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'
class ApplyToType(str, Enum):
    All = 'All'
    Agreement = 'Agreement'
    Project = 'Project'
    ProjectPhase = 'ProjectPhase'
    SalesOrder = 'SalesOrder'
    Ticket = 'Ticket'

class InvoiceModel(ConnectWiseModel):
    id: int | None
    invoice_number: str | None
    type: InvoiceModelType | None
    status: BillingStatusReferenceModel | None
    company: CompanyReferenceModel | None
    bill_to_company: CompanyReferenceModel | None
    ship_to_company: CompanyReferenceModel | None
    account_number: str | None
    apply_to_type: ApplyToType | None
    apply_to_id: int | None
    attention: str | None
    ship_to_attention: str | None
    billing_site: SiteReferenceModel | None
    billing_site_address_line1: str | None
    billing_site_address_line2: str | None
    billing_site_city: str | None
    billing_site_state: str | None
    billing_site_zip: str | None
    billing_site_country: str | None
    shipping_site: SiteReferenceModel | None
    shipping_site_address_line1: str | None
    shipping_site_address_line2: str | None
    shipping_site_city: str | None
    shipping_site_state: str | None
    shipping_site_zip: str | None
    shipping_site_country: str | None
    billing_terms: BillingTermsReferenceModel | None
    reference: str | None
    customer_p_o: str | None
    template_setup_id: int | None
    invoice_template: InvoiceTemplateDetailReferenceModel | None
    email_template_id: int | None
    add_to_batch_email_list: bool | None
    date: str | None
    restrict_downpayment_flag: bool | None
    location_id: int | None
    department_id: int | None
    territory_id: int | None
    top_comment: str | None
    bottom_comment: str | None
    taxable_flag: bool | None
    tax_code: TaxCodeReferenceModel | None
    internal_notes: str | None
    downpayment_previously_taxed_flag: bool | None
    service_total: float | None
    override_down_payment_amount_flag: bool | None
    currency: CurrencyReferenceModel | None
    due_date: str | None
    expense_total: float | None
    product_total: float | None
    previous_progress_applied: float | None
    service_adjustment_amount: float | None
    agreement_amount: float | None
    downpayment_applied: float | None
    subtotal: float | None
    total: float | None
    remaining_downpayment: float | None
    sales_tax: float | None
    adjustment_reason: str | None
    adjusted_by: str | None
    payments: float | None
    credits: float | None
    balance: float | None
    special_invoice_flag: bool | None
    billing_setup_reference: BillingSetupReferenceModel | None
    ticket: TicketReferenceModel | None
    project: ProjectReferenceModel | None
    phase: ProjectPhaseReferenceModel | None
    sales_order: SalesOrderReferenceModel | None
    agreement: AgreementReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True