from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class TaxIntegrationType(str, Enum):
    Avalara = 'Avalara'

class TaxIntegrationModel(ConnectWiseModel):
    tax_integration_type: TaxIntegrationType | None
    id: int | None
    account_number: str | None
    license_key: str | None
    service_url: str | None
    company_code: str | None
    time_tax_code: str | None
    expense_tax_code: str | None
    product_tax_code: str | None
    invoice_amount_tax_code: str | None
    enabled_flag: bool | None
    commit_transactions_flag: bool | None
    sales_invoice_flag: bool | None
    freight_tax_code: str | None
    accounting_integration_flag: bool | None
    tax_line_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True