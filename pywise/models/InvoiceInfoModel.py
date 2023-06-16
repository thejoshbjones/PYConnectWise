from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.InvoiceModel import InvoiceModel
from pywise.models.InvoiceTemplateModel import InvoiceTemplateModel
from pywise.models.ProductItemModel import ProductItemModel
from pywise.models.ProductComponentModel import ProductComponentModel
from pywise.models.ExpenseEntryModel import ExpenseEntryModel
from pywise.models.TimeEntryModel import TimeEntryModel
from pywise.models.DocumentInfoModel import DocumentInfoModel
from pywise.models.BillingSetupModel import BillingSetupModel
from pywise.models.AgreementBillingInfoModel import AgreementBillingInfoModel

class InvoiceInfoModel(ConnectWiseModel):
    id: int | None
    invoice: InvoiceModel | None
    invoice_template: InvoiceTemplateModel | None
    products: list[ProductItemModel] | None
    bundled_components_info: list[ProductComponentModel] | None
    expenses: list[ExpenseEntryModel] | None
    time_entries: list[TimeEntryModel] | None
    logo: DocumentInfoModel | None
    billing_setup: BillingSetupModel | None
    agreement_billing_info: list[AgreementBillingInfoModel] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True