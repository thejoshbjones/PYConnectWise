from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.OpportunityTypeReferenceModel import OpportunityTypeReferenceModel
from pywise.models.OpportunityStageReferenceModel import OpportunityStageReferenceModel
from pywise.models.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pywise.models.OpportunityPriorityReferenceModel import OpportunityPriorityReferenceModel
from pywise.models.OpportunityProbabilityReferenceModel import OpportunityProbabilityReferenceModel
from pywise.models.OpportunityRatingReferenceModel import OpportunityRatingReferenceModel
from pywise.models.CampaignReferenceModel import CampaignReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel

class OpportunityModel(ConnectWiseModel):
    id: int | None
    name: str | None
    expected_close_date: str | None
    type: OpportunityTypeReferenceModel | None
    stage: OpportunityStageReferenceModel | None
    status: OpportunityStatusReferenceModel | None
    priority: OpportunityPriorityReferenceModel | None
    notes: str | None
    probability: OpportunityProbabilityReferenceModel | None
    source: str | None
    rating: OpportunityRatingReferenceModel | None
    campaign: CampaignReferenceModel | None
    primary_sales_rep: MemberReferenceModel | None
    secondary_sales_rep: MemberReferenceModel | None
    location_id: int | None
    business_unit_id: int | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    site: SiteReferenceModel | None
    customer_p_o: str | None
    pipeline_change_date: str | None
    date_became_lead: str | None
    closed_date: str | None
    closed_by: MemberReferenceModel | None
    total_sales_tax: float | None
    ship_to_company: CompanyReferenceModel | None
    ship_to_contact: ContactReferenceModel | None
    ship_to_site: SiteReferenceModel | None
    bill_to_company: CompanyReferenceModel | None
    bill_to_contact: ContactReferenceModel | None
    bill_to_site: SiteReferenceModel | None
    billing_terms: BillingTermsReferenceModel | None
    tax_code: TaxCodeReferenceModel | None
    currency: CurrencyReferenceModel | None
    company_location_id: int | None
    technical_contact: ContactReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True