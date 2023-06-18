from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class BillExpenses(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class InvoiceMarkupOption(str, Enum):
    Amount = 'Amount'
    Mile = 'Mile'
    Percent = 'Percent'

class ExpenseTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    amount_caption: str | None
    reimbursement_rate: float | None
    bill_expenses: BillExpenses | None
    invoice_markup_option: InvoiceMarkupOption | None
    invoice_markup_amount: float | None
    advanced_amount_flag: bool | None
    mileage_flag: bool | None
    quantity_flag: bool | None
    inactive_flag: bool | None
    max_amount: float | None
    integration_x_ref: str | None
    default_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True