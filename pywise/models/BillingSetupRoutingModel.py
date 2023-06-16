from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.MemberReferenceModel import MemberReferenceModel
class InvoiceRule(str, Enum):
    All = 'All'
    Standard = 'Standard'
    Project = 'Project'
    Agreement = 'Agreement'
class RoutingRule(str, Enum):
    Account = 'Account'
    Territory = 'Territory'
    Creator = 'Creator'
    Department = 'Department'
    Location = 'Location'
    Member = 'Member'
    Project = 'Project'
    Sales = 'Sales'

class BillingSetupRoutingModel(ConnectWiseModel):
    id: int | None
    sequence_number: int | None
    invoice_rule: InvoiceRule | None
    routing_rule: RoutingRule | None
    member: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True