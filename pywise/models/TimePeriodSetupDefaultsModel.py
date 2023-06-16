from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class TimePeriodSetupDefaultsModel(ConnectWiseModel):

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True