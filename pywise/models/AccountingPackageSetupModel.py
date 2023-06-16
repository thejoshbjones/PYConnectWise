from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AccountingPackageReferenceModel import AccountingPackageReferenceModel
from enum import Enum
class InvoiceFormat(str, Enum):
    Default = 'Default'
    Condensed = 'Condensed'
    Detailed = 'Detailed'
class ExpenseFormat(str, Enum):
    Default = 'Default'
    Condensed = 'Condensed'

class AccountingPackageSetupModel(ConnectWiseModel):
    id: int | None
    accounting_package: AccountingPackageReferenceModel | None
    direct_transfer_flag: bool | None
    include_invoices_flag: bool | None
    invoice_format: InvoiceFormat | None
    include_expenses_flag: bool | None
    transfer_expenses_as_bill_flag: bool | None
    expense_format: ExpenseFormat | None
    suppress_memo_flag: bool | None
    sync_payment_info_flag: bool | None
    include_sales_tax_flag: bool | None
    enable_tax_groups_flag: bool | None
    zero_dollar_tax_amounts_flag: bool | None
    include_items_flag: bool | None
    inventory_s_o_h_flag: bool | None
    send_component_amount_flag: bool | None
    send_uom_flag: bool | None
    include_cogs_entries_flag: bool | None
    include_cogs_drop_ship_flag: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True