from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.PortalConfigurationReferenceModel import PortalConfigurationReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.PortalConfigurationPaymentProcessorReferenceModel import PortalConfigurationPaymentProcessorReferenceModel

class PortalConfigurationInvoiceSetupModel(ConnectWiseModel):
    id: int
    portal_configuration: PortalConfigurationReferenceModel
    display_inv_pmt_flag: bool
    allow_inv_pmt_flag: bool
    location: SystemLocationReferenceModel
    payment_processor: PortalConfigurationPaymentProcessorReferenceModel
    login: str
    password: str
    url_override: str
    billing_status_ids: list[int]
    add_all_statuses: bool
    remove_all_statuses: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True