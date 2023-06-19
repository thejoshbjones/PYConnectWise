from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.GLExportSettingsModel import GLExportSettingsModel
from pywise.models.manage.GLExportVendorModel import GLExportVendorModel
from pywise.models.manage.GLExportCustomerModel import GLExportCustomerModel
from pywise.models.manage.GLExportTransactionModel import GLExportTransactionModel
from pywise.models.manage.GLExportExpenseModel import GLExportExpenseModel
from pywise.models.manage.GLExportExpenseBillModel import GLExportExpenseBillModel
from pywise.models.manage.GLExportPurchaseTransactionModel import GLExportPurchaseTransactionModel
from pywise.models.manage.GLExportAdjustmentTransactionModel import GLExportAdjustmentTransactionModel
from pywise.models.manage.GLExportInventoryTransferModel import GLExportInventoryTransferModel

class GLExportModel(ConnectWiseModel):
    export_settings: GLExportSettingsModel
    vendors: list[GLExportVendorModel]
    customers: list[GLExportCustomerModel]
    transactions: list[GLExportTransactionModel]
    expenses: list[GLExportExpenseModel]
    expense_bills: list[GLExportExpenseBillModel]
    purchase_transactions: list[GLExportPurchaseTransactionModel]
    adjustment_transactions: list[GLExportAdjustmentTransactionModel]
    inventory_transfers: list[GLExportInventoryTransferModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True