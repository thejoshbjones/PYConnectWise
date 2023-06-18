from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel
from pywise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel

class ManagementItSolutionAgreementInterfaceParameterModel(ConnectWiseModel):
    id: int | None
    managed_devices_integration: ManagedDevicesIntegrationReferenceModel | None
    agreement_type: AgreementTypeReferenceModel | None
    server_product: IvItemReferenceModel | None
    workstation_product: IvItemReferenceModel | None
    spam_stats_product: IvItemReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True