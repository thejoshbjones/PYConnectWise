from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Task(str, Enum):
    All = 'All'
    Closed = 'Closed'
    Open = 'Open'

class ServiceSignoffModel(ConnectWiseModel):
    id: int | None
    name: str | None
    default_flag: bool | None
    visible_logo_flag: bool | None
    company_info_flag: bool | None
    billing_terms_flag: bool | None
    summary_flag: bool | None
    discussion_flag: bool | None
    task_flag: bool | None
    task: Task | None
    configurations_flag: bool | None
    internal_notes_flag: bool | None
    resolution_flag: bool | None
    time_flag: bool | None
    time_member_flag: bool | None
    time_date_flag: bool | None
    time_start_end_flag: bool | None
    time_bill_flag: bool | None
    time_hours_flag: bool | None
    time_rate_flag: bool | None
    time_extended_amount_flag: bool | None
    time_work_type_flag: bool | None
    time_agreement_flag: bool | None
    time_notes_flag: bool | None
    time_manual_flag: bool | None
    time_manual_entry: int | None
    time_tax_flag: bool | None
    expense_flag: bool | None
    expense_date_flag: bool | None
    expense_member_flag: bool | None
    expense_type_flag: bool | None
    expense_bill_flag: bool | None
    expense_amount_flag: bool | None
    expense_agreement_flag: bool | None
    expense_notes_flag: bool | None
    expense_tax_flag: bool | None
    expense_manual_flag: bool | None
    expense_manual_entry: int | None
    product_flag: bool | None
    product_description_flag: bool | None
    product_bill_flag: bool | None
    product_quantity_flag: bool | None
    product_price_flag: bool | None
    product_extended_amount_flag: bool | None
    product_agreement_flag: bool | None
    product_manual_flag: bool | None
    product_manual_entry: int | None
    product_tax_flag: bool | None
    technician_signoff_flag: bool | None
    customer_signoff_text_flag: bool | None
    customer_signoff_text: str | None
    customer_signoff_fields_flag: bool | None
    billing_methods_text_flag: bool | None
    billing_methods_text: str | None
    credit_card_fields_flag: bool | None
    default_f_f_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True