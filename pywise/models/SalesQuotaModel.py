from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pywise.models.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel

class SalesQuotaModel(ConnectWiseModel):
    id: int | None
    member: MemberReferenceModel | None
    forecast_year: int | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    category: ProductCategoryReferenceModel | None
    sub_category: ProductSubCategoryReferenceModel | None
    january_revenue: float | None
    january_margin: float | None
    february_revenue: float | None
    february_margin: float | None
    march_revenue: float | None
    march_margin: float | None
    april_revenue: float | None
    april_margin: float | None
    may_revenue: float | None
    may_margin: float | None
    june_revenue: float | None
    june_margin: float | None
    july_revenue: float | None
    july_margin: float | None
    august_revenue: float | None
    august_margin: float | None
    september_revenue: float | None
    september_margin: float | None
    october_revenue: float | None
    october_margin: float | None
    november_revenue: float | None
    november_margin: float | None
    december_revenue: float | None
    december_margin: float | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True