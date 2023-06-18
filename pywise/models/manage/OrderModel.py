from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.OrderStatusReferenceModel import OrderStatusReferenceModel
from pywise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class OrderModel(ConnectWiseModel):
    id: int | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    phone: str | None
    phone_ext: str | None
    email: str | None
    site: SiteReferenceModel | None
    status: OrderStatusReferenceModel | None
    opportunity: OpportunityReferenceModel | None
    order_date: str | None
    due_date: str | None
    billing_terms: BillingTermsReferenceModel | None
    tax_code: TaxCodeReferenceModel | None
    po_number: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    sales_rep: MemberReferenceModel | None
    notes: str | None
    bill_closed_flag: bool | None
    bill_shipped_flag: bool | None
    restrict_downpayment_flag: bool | None
    description: str | None
    top_comment_flag: bool | None
    bottom_comment_flag: bool | None
    ship_to_company: CompanyReferenceModel | None
    ship_to_contact: ContactReferenceModel | None
    ship_to_site: SiteReferenceModel | None
    bill_to_company: CompanyReferenceModel | None
    bill_to_contact: ContactReferenceModel | None
    bill_to_site: SiteReferenceModel | None
    product_ids: list[int] | None
    document_ids: list[int] | None
    invoice_ids: list[int] | None
    config_ids: list[int] | None
    total: float | None
    tax_total: float | None
    currency: CurrencyReferenceModel | None
    company_location: SystemLocationReferenceModel | None
    sub_total: float | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True