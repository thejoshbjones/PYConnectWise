from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel

class GLExportVendorModel(ConnectWiseModel):
    member: MemberReferenceModel
    vendor: CompanyReferenceModel
    vendor_number: str
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    account_number: str
    billing_terms: BillingTermsReferenceModel
    due_days: int
    site: SiteReferenceModel
    tax_code: TaxCodeReferenceModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True