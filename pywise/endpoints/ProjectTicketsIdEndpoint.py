from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectTicketsIdActivitiesEndpoint import ProjectTicketsIdActivitiesEndpoint
from pywise.endpoints.ProjectTicketsIdAllNotesEndpoint import ProjectTicketsIdAllNotesEndpoint
from pywise.endpoints.ProjectTicketsIdConfigurationsEndpoint import ProjectTicketsIdConfigurationsEndpoint
from pywise.endpoints.ProjectTicketsIdConvertEndpoint import ProjectTicketsIdConvertEndpoint
from pywise.endpoints.ProjectTicketsIdDocumentsEndpoint import ProjectTicketsIdDocumentsEndpoint
from pywise.endpoints.ProjectTicketsIdNotesEndpoint import ProjectTicketsIdNotesEndpoint
from pywise.endpoints.ProjectTicketsIdProductsEndpoint import ProjectTicketsIdProductsEndpoint
from pywise.endpoints.ProjectTicketsIdScheduleentriesEndpoint import ProjectTicketsIdScheduleentriesEndpoint
from pywise.endpoints.ProjectTicketsIdTasksEndpoint import ProjectTicketsIdTasksEndpoint
from pywise.endpoints.ProjectTicketsIdTimeentriesEndpoint import ProjectTicketsIdTimeentriesEndpoint
from pywise.models.ProjectTicketModel import ProjectTicketModel

class ProjectTicketsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.activities = self.register_child_endpoint(
            ProjectTicketsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.allNotes = self.register_child_endpoint(
            ProjectTicketsIdAllNotesEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self.register_child_endpoint(
            ProjectTicketsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.convert = self.register_child_endpoint(
            ProjectTicketsIdConvertEndpoint(client, parent_endpoint=self)
        )
        self.documents = self.register_child_endpoint(
            ProjectTicketsIdDocumentsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            ProjectTicketsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.products = self.register_child_endpoint(
            ProjectTicketsIdProductsEndpoint(client, parent_endpoint=self)
        )
        self.scheduleentries = self.register_child_endpoint(
            ProjectTicketsIdScheduleentriesEndpoint(client, parent_endpoint=self)
        )
        self.tasks = self.register_child_endpoint(
            ProjectTicketsIdTasksEndpoint(client, parent_endpoint=self)
        )
        self.timeentries = self.register_child_endpoint(
            ProjectTicketsIdTimeentriesEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectTicketModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectTicketModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ProjectTicketModel:
        return self._parse_one(ProjectTicketModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ProjectTicketModel:
        return self._parse_one(ProjectTicketModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ProjectTicketModel:
        return self._parse_one(ProjectTicketModel, super().make_request("PATCH", params=params))
        