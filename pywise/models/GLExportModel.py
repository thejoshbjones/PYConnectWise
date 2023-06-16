from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.GLExportSettingsModel import GLExportSettingsModel
from pywise.models.GLExportVendorModel import GLExportVendorModel
from pywise.models.GLExportCustomerModel import GLExportCustomerModel
from pywise.models.GLExportTransactionModel import GLExportTransactionModel
from pywise.models.GLExportExpenseModel import GLExportExpenseModel
from pywise.models.GLExportExpenseBillModel import GLExportExpenseBillModel
from pywise.models.GLExportPurchaseTransactionModel import GLExportPurchaseTransactionModel
from pywise.models.GLExportAdjustmentTransactionModel import GLExportAdjustmentTransactionModel
from pywise.models.GLExportInventoryTransferModel import GLExportInventoryTransferModel

class GLExportModel(ConnectWiseModel):
    export_settings: GLExportSettingsModel | None
    vendors: list[GLExportVendorModel] | None
    customers: list[GLExportCustomerModel] | None
    transactions: list[GLExportTransactionModel] | None
    expenses: list[GLExportExpenseModel] | None
    expense_bills: list[GLExportExpenseBillModel] | None
    purchase_transactions: list[GLExportPurchaseTransactionModel] | None
    adjustment_transactions: list[GLExportAdjustmentTransactionModel] | None
    inventory_transfers: list[GLExportInventoryTransferModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True