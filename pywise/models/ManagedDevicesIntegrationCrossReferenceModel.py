from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel
from pywise.models.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel

class ManagedDevicesIntegrationCrossReferenceModel(ConnectWiseModel):
    id: int | None
    managed_devices_integration: ManagedDevicesIntegrationReferenceModel | None
    vendor_type: str | None
    vendor_level: str | None
    agreement_type: AgreementTypeReferenceModel | None
    product: IvItemReferenceModel | None
    configuration_type: ConfigurationTypeReferenceModel | None
    inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True