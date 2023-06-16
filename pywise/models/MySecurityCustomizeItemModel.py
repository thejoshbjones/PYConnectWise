from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class CustomizeIdentifier(str, Enum):
    CompanyReports = 'CompanyReports'
    FinanceReports = 'FinanceReports'
    MarketingReports = 'MarketingReports'
    ProcurementReports = 'ProcurementReports'
    ProjectReports = 'ProjectReports'
    SalesReports = 'SalesReports'
    ServiceReports = 'ServiceReports'
    SystemReports = 'SystemReports'
    TimeAndExpenseReports = 'TimeAndExpenseReports'
    CompanyConfigurations = 'CompanyConfigurations'
    FinanceAgreements = 'FinanceAgreements'
    ProjectScheduling = 'ProjectScheduling'
    ServiceResourceScheduling = 'ServiceResourceScheduling'
    SystemManageHostedApi = 'SystemManageHostedApi'
    SystemMyAccount = 'SystemMyAccount'
    SystemCustomMenuEntry = 'SystemCustomMenuEntry'
    SystemMassMaintenance = 'SystemMassMaintenance'
    SystemTableSetup = 'SystemTableSetup'

class MySecurityCustomizeItemModel(ConnectWiseModel):
    id: int | None
    customize_identifier: CustomizeIdentifier | None
    item_identifier: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True