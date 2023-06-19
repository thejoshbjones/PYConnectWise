from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ForecastItemModel import ForecastItemModel
from pywise.models.manage.ProductRevenueReferenceModel import ProductRevenueReferenceModel
from pywise.models.manage.ServiceRevenueReferenceModel import ServiceRevenueReferenceModel
from pywise.models.manage.AgreementRevenueReferenceModel import AgreementRevenueReferenceModel
from pywise.models.manage.TimeRevenueReferenceModel import TimeRevenueReferenceModel
from pywise.models.manage.ExpenseRevenueReferenceModel import ExpenseRevenueReferenceModel
from pywise.models.manage.ForecastRevenueReferenceModel import ForecastRevenueReferenceModel
from pywise.models.manage.InclusiveRevenueReferenceModel import InclusiveRevenueReferenceModel
from pywise.models.manage.WonRevenueReferenceModel import WonRevenueReferenceModel
from pywise.models.manage.LostRevenueReferenceModel import LostRevenueReferenceModel
from pywise.models.manage.OpenRevenueReferenceModel import OpenRevenueReferenceModel
from pywise.models.manage.Other1RevenueReferenceModel import Other1RevenueReferenceModel
from pywise.models.manage.Other2RevenueReferenceModel import Other2RevenueReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class ForecastModel(ConnectWiseModel):
    id: int
    forecast_items: list[ForecastItemModel]
    product_revenue: ProductRevenueReferenceModel
    service_revenue: ServiceRevenueReferenceModel
    agreement_revenue: AgreementRevenueReferenceModel
    time_revenue: TimeRevenueReferenceModel
    expense_revenue: ExpenseRevenueReferenceModel
    forecast_revenue_totals: ForecastRevenueReferenceModel
    inclusive_revenue_totals: InclusiveRevenueReferenceModel
    recurring_total: float
    won_revenue: WonRevenueReferenceModel
    lost_revenue: LostRevenueReferenceModel
    open_revenue: OpenRevenueReferenceModel
    other_revenue1: Other1RevenueReferenceModel
    other_revenue2: Other2RevenueReferenceModel
    sales_tax_revenue: float
    forecast_total_with_taxes: float
    expected_probability: int
    tax_code: TaxCodeReferenceModel
    billing_terms: BillingTermsReferenceModel
    currency: CurrencyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True