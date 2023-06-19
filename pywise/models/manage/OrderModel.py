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
    id: int
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    phone: str
    phone_ext: str
    email: str
    site: SiteReferenceModel
    status: OrderStatusReferenceModel
    opportunity: OpportunityReferenceModel
    order_date: str
    due_date: str
    billing_terms: BillingTermsReferenceModel
    tax_code: TaxCodeReferenceModel
    po_number: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    sales_rep: MemberReferenceModel
    notes: str
    bill_closed_flag: bool
    bill_shipped_flag: bool
    restrict_downpayment_flag: bool
    description: str
    top_comment_flag: bool
    bottom_comment_flag: bool
    ship_to_company: CompanyReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    product_ids: list[int]
    document_ids: list[int]
    invoice_ids: list[int]
    config_ids: list[int]
    total: float
    tax_total: float
    currency: CurrencyReferenceModel
    company_location: SystemLocationReferenceModel
    sub_total: float
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True