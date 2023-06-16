from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
class DefaultSpecialInvoiceType(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'

class TimeExpenseModel(ConnectWiseModel):
    id: int | None
    tier1_approval_flag: bool | None
    tier2_approval_flag: bool | None
    disable_time_entry_flag: bool | None
    require_time_note_flag: bool | None
    require_expense_note_flag: bool | None
    rounding_factor: float | None
    invoice_start: int | None
    default_special_invoice_type: DefaultSpecialInvoiceType | None
    internal_company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True