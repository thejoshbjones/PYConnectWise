from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.InvoiceModel import InvoiceModel
from pywise.models.manage.InvoiceTemplateModel import InvoiceTemplateModel
from pywise.models.manage.ProductItemModel import ProductItemModel
from pywise.models.manage.ProductComponentModel import ProductComponentModel
from pywise.models.manage.ExpenseEntryModel import ExpenseEntryModel
from pywise.models.manage.TimeEntryModel import TimeEntryModel
from pywise.models.manage.DocumentInfoModel import DocumentInfoModel
from pywise.models.manage.BillingSetupModel import BillingSetupModel
from pywise.models.manage.AgreementBillingInfoModel import AgreementBillingInfoModel

class InvoiceInfoModel(ConnectWiseModel):
    id: int
    invoice: InvoiceModel
    invoice_template: InvoiceTemplateModel
    products: list[ProductItemModel]
    bundled_components_info: list[ProductComponentModel]
    expenses: list[ExpenseEntryModel]
    time_entries: list[TimeEntryModel]
    logo: DocumentInfoModel
    billing_setup: BillingSetupModel
    agreement_billing_info: list[AgreementBillingInfoModel]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True