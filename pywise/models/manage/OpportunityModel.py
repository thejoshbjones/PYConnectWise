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