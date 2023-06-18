from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.MemberDeactivationSalesActivityModel import MemberDeactivationSalesActivityModel
from pywise.models.manage.MemberDeactivationServiceTeamModel import MemberDeactivationServiceTeamModel
from pywise.models.manage.MemberDeactivationCompanyTeamModel import MemberDeactivationCompanyTeamModel
from pywise.models.manage.MemberDeactivationWorkflowModel import MemberDeactivationWorkflowModel
from pywise.models.manage.MemberDeactivationStatusWorkflowModel import MemberDeactivationStatusWorkflowModel
from pywise.models.manage.MemberDeactivationServiceTemplateModel import MemberDeactivationServiceTemplateModel
from pywise.models.manage.MemberDeactivationOpportunityModel import MemberDeactivationOpportunityModel
from pywise.models.manage.MemberDeactivationSalesTeamModel import MemberDeactivationSalesTeamModel
from pywise.models.manage.MemberDeactivationProjectManagerModel import MemberDeactivationProjectManagerModel
from pywise.models.manage.MemberDeactivationProjectManagerModel import MemberDeactivationProjectManagerModel
from pywise.models.manage.MemberDeactivationProjectManagerModel import MemberDeactivationProjectManagerModel
from pywise.models.manage.MemberDeactivationKnowledgebaseArticleModel import MemberDeactivationKnowledgebaseArticleModel
from pywise.models.manage.MemberDeactivationMyCompanyPresidentRoleModel import MemberDeactivationMyCompanyPresidentRoleModel
from pywise.models.manage.MemberDeactivationMyCompanyCOORoleModel import MemberDeactivationMyCompanyCOORoleModel
from pywise.models.manage.MemberDeactivationMyCompanyControllerRoleModel import MemberDeactivationMyCompanyControllerRoleModel
from pywise.models.manage.MemberDeactivationMyCompanyDispatchRoleModel import MemberDeactivationMyCompanyDispatchRoleModel
from pywise.models.manage.MemberDeactivationMyCompanyServiceManagerRoleModel import MemberDeactivationMyCompanyServiceManagerRoleModel
from pywise.models.manage.MemberDeactivationMyCompanyDutyManagerRoleModel import MemberDeactivationMyCompanyDutyManagerRoleModel
from pywise.models.manage.MemberDeactivationDepartmentMananagerModel import MemberDeactivationDepartmentMananagerModel
from pywise.models.manage.MemberDeactivationDispatchMemberModel import MemberDeactivationDispatchMemberModel
from pywise.models.manage.MemberDeactivationServiceMangerModel import MemberDeactivationServiceMangerModel
from pywise.models.manage.MemberDeactivationDutyManagerModel import MemberDeactivationDutyManagerModel
from pywise.models.manage.MemberDeactivationSendFromEmailNotifyModel import MemberDeactivationSendFromEmailNotifyModel

class MemberDeactivationModel(ConnectWiseModel):
    activity: MemberDeactivationSalesActivityModel | None
    service_team: MemberDeactivationServiceTeamModel | None
    company_team: list[MemberDeactivationCompanyTeamModel] | None
    workflow_email: MemberDeactivationWorkflowModel | None
    service_status_workflow: list[MemberDeactivationStatusWorkflowModel] | None
    ticket_template: MemberDeactivationServiceTemplateModel | None
    opportunity: MemberDeactivationOpportunityModel | None
    sales_team: MemberDeactivationSalesTeamModel | None
    project_manager: MemberDeactivationProjectManagerModel | None
    project_time_approver: MemberDeactivationProjectManagerModel | None
    project_expense_approver: MemberDeactivationProjectManagerModel | None
    knowledge_base_article: MemberDeactivationKnowledgebaseArticleModel | None
    my_company_president: MemberDeactivationMyCompanyPresidentRoleModel | None
    my_company_c_o_o: MemberDeactivationMyCompanyCOORoleModel | None
    my_company_controller: MemberDeactivationMyCompanyControllerRoleModel | None
    my_company_dispatch: MemberDeactivationMyCompanyDispatchRoleModel | None
    my_company_service_manager: MemberDeactivationMyCompanyServiceManagerRoleModel | None
    my_company_duty_manager_role: MemberDeactivationMyCompanyDutyManagerRoleModel | None
    department_manager: MemberDeactivationDepartmentMananagerModel | None
    dispatch_member: MemberDeactivationDispatchMemberModel | None
    service_manager: MemberDeactivationServiceMangerModel | None
    duty_manager: MemberDeactivationDutyManagerModel | None
    send_from_email_notify: MemberDeactivationSendFromEmailNotifyModel | None
    delete_open_time_sheets_flag: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True