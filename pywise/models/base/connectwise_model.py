from __future__ import annotations
from pydantic import BaseModel
from pywise.models.utils.naming import to_camel_case

class ConnectWiseModel(BaseModel):

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True