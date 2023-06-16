from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ForecastItemModel import ForecastItemModel
from pywise.models.ProductRevenueReferenceModel import ProductRevenueReferenceModel
from pywise.models.ServiceRevenueReferenceModel import ServiceRevenueReferenceModel
from pywise.models.AgreementRevenueReferenceModel import AgreementRevenueReferenceModel
from pywise.models.TimeRevenueReferenceModel import TimeRevenueReferenceModel
from pywise.models.ExpenseRevenueReferenceModel import ExpenseRevenueReferenceModel
from pywise.models.ForecastRevenueReferenceModel import ForecastRevenueReferenceModel
from pywise.models.InclusiveRevenueReferenceModel import InclusiveRevenueReferenceModel
from pywise.models.WonRevenueReferenceModel import WonRevenueReferenceModel
from pywise.models.LostRevenueReferenceModel import LostRevenueReferenceModel
from pywise.models.OpenRevenueReferenceModel import OpenRevenueReferenceModel
from pywise.models.Other1RevenueReferenceModel import Other1RevenueReferenceModel
from pywise.models.Other2RevenueReferenceModel import Other2RevenueReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class ForecastModel(ConnectWiseModel):
    id: int | None
    forecast_items: list[ForecastItemModel] | None
    product_revenue: ProductRevenueReferenceModel | None
    service_revenue: ServiceRevenueReferenceModel | None
    agreement_revenue: AgreementRevenueReferenceModel | None
    time_revenue: TimeRevenueReferenceModel | None
    expense_revenue: ExpenseRevenueReferenceModel | None
    forecast_revenue_totals: ForecastRevenueReferenceModel | None
    inclusive_revenue_totals: InclusiveRevenueReferenceModel | None
    recurring_total: float | None
    won_revenue: WonRevenueReferenceModel | None
    lost_revenue: LostRevenueReferenceModel | None
    open_revenue: OpenRevenueReferenceModel | None
    other_revenue1: Other1RevenueReferenceModel | None
    other_revenue2: Other2RevenueReferenceModel | None
    sales_tax_revenue: float | None
    forecast_total_with_taxes: float | None
    expected_probability: int | None
    tax_code: TaxCodeReferenceModel | None
    billing_terms: BillingTermsReferenceModel | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True