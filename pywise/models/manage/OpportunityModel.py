from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.OpportunityTypeReferenceModel import OpportunityTypeReferenceModel
from pywise.models.manage.OpportunityStageReferenceModel import OpportunityStageReferenceModel
from pywise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.manage.OpportunityPriorityReferenceModel import OpportunityPriorityReferenceModel
from pywise.models.manage.OpportunityProbabilityReferenceModel import OpportunityProbabilityReferenceModel
from pywise.models.manage.OpportunityRatingReferenceModel import OpportunityRatingReferenceModel
from pywise.models.manage.CampaignReferenceModel import CampaignReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class OpportunityModel(ConnectWiseModel):
    id: int
    name: str
    expected_close_date: str
    type: OpportunityTypeReferenceModel
    stage: OpportunityStageReferenceModel
    status: OpportunityStatusReferenceModel
    priority: OpportunityPriorityReferenceModel
    notes: str
    probability: OpportunityProbabilityReferenceModel
    source: str
    rating: OpportunityRatingReferenceModel
    campaign: CampaignReferenceModel
    primary_sales_rep: MemberReferenceModel
    secondary_sales_rep: MemberReferenceModel
    location_id: int
    business_unit_id: int
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    customer_p_o: str
    pipeline_change_date: str
    date_became_lead: str
    closed_date: str
    closed_by: MemberReferenceModel
    total_sales_tax: float
    ship_to_company: CompanyReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    billing_terms: BillingTermsReferenceModel
    tax_code: TaxCodeReferenceModel
    currency: CurrencyReferenceModel
    company_location_id: int
    technical_contact: ContactReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True