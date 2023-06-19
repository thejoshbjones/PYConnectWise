from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from enum import Enum
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.manage.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pywise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pywise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
class BillingMethod(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'
class CommissionBasis(str, Enum):
    GrossProfit = 'GrossProfit'
    SalesAmount = 'SalesAmount'
class InvoiceOption(str, Enum):
    AllInvoices = 'AllInvoices'
    PaidInvoices = 'PaidInvoices'

class CommissionModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    commission_percent: float
    date_start: str
    date_end: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    company: CompanyReferenceModel
    site: SiteReferenceModel
    agreement: AgreementReferenceModel
    project: ProjectReferenceModel
    service_board: BoardReferenceModel
    ticket: TicketReferenceModel
    territory: SystemLocationReferenceModel
    billing_method: BillingMethod
    service_type: ServiceTypeReferenceModel
    project_board: ProjectBoardReferenceModel
    project_type: ProjectTypeReferenceModel
    agreement_type: AgreementTypeReferenceModel
    number_of_months: int
    product_category: ProductCategoryReferenceModel
    product_sub_category: ProductSubCategoryReferenceModel
    item: IvItemReferenceModel
    commission_basis: CommissionBasis
    invoice_option: InvoiceOption
    services_flag: bool
    agreements_flag: bool
    products_flag: bool
    my_opportunities_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True