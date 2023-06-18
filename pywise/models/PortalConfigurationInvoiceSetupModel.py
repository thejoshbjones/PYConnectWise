from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.PortalConfigurationReferenceModel import PortalConfigurationReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.PortalConfigurationPaymentProcessorReferenceModel import PortalConfigurationPaymentProcessorReferenceModel

class PortalConfigurationInvoiceSetupModel(ConnectWiseModel):
    id: int | None
    portal_configuration: PortalConfigurationReferenceModel | None
    display_inv_pmt_flag: bool | None
    allow_inv_pmt_flag: bool | None
    location: SystemLocationReferenceModel | None
    payment_processor: PortalConfigurationPaymentProcessorReferenceModel | None
    login: str | None
    password: str | None
    url_override: str | None
    billing_status_ids: list[int] | None
    add_all_statuses: bool | None
    remove_all_statuses: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True