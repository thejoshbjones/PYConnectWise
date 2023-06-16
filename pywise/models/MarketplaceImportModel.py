from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class MarketplaceImportType(str, Enum):
    Agreements = 'Agreements'
    Configurations = 'Configurations'
    CRMSurveys = 'CRMSurveys'
    CustomReports = 'CustomReports'
    CustomerPortalTypes = 'CustomerPortalTypes'
    HTMLEmailTemplates = 'HTMLEmailTemplates'
    Products = 'Products'
    ProjectBoards = 'ProjectBoards'
    ProjectTemplates = 'ProjectTemplates'
    ReportWriterReports = 'ReportWriterReports'
    ServiceBoards = 'ServiceBoards'
    TicketTemplates = 'TicketTemplates'
    Views = 'Views'

class MarketplaceImportModel(ConnectWiseModel):
    id: int | None
    marketplace_import_type: MarketplaceImportType | None
    marketplace_object: list[Any] | None
    required_fields: list[str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True