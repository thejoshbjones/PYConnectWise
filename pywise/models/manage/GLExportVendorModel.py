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
    member: MemberReferenceModel | None
    vendor: CompanyReferenceModel | None
    vendor_number: str | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    account_number: str | None
    billing_terms: BillingTermsReferenceModel | None
    due_days: int | None
    site: SiteReferenceModel | None
    tax_code: TaxCodeReferenceModel | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True