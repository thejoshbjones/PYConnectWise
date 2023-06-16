from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.ProjectPhaseStatusesEndpoint import ProjectPhaseStatusesEndpoint
from pywise.endpoints.ProjectProjectsEndpoint import ProjectProjectsEndpoint
from pywise.endpoints.ProjectProjectTypesEndpoint import ProjectProjectTypesEndpoint
from pywise.endpoints.ProjectSecurityRolesEndpoint import ProjectSecurityRolesEndpoint
from pywise.endpoints.ProjectStatusesEndpoint import ProjectStatusesEndpoint
from pywise.endpoints.ProjectStatusIndicatorsEndpoint import ProjectStatusIndicatorsEndpoint
from pywise.endpoints.ProjectTicketsEndpoint import ProjectTicketsEndpoint

class ProjectEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "project")
        
        self.phaseStatuses = self.register_child_endpoint(
            ProjectPhaseStatusesEndpoint(client, parent_endpoint=self)
        )
        self.projects = self.register_child_endpoint(
            ProjectProjectsEndpoint(client, parent_endpoint=self)
        )
        self.projectTypes = self.register_child_endpoint(
            ProjectProjectTypesEndpoint(client, parent_endpoint=self)
        )
        self.securityRoles = self.register_child_endpoint(
            ProjectSecurityRolesEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            ProjectStatusesEndpoint(client, parent_endpoint=self)
        )
        self.statusIndicators = self.register_child_endpoint(
            ProjectStatusIndicatorsEndpoint(client, parent_endpoint=self)
        )
        self.tickets = self.register_child_endpoint(
            ProjectTicketsEndpoint(client, parent_endpoint=self)
        )