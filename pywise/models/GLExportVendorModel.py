from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel

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