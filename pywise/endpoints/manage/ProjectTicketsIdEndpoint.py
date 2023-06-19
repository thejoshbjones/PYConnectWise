from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProjectTicketsIdActivitiesEndpoint import ProjectTicketsIdActivitiesEndpoint
from pywise.endpoints.manage.ProjectTicketsIdAllNotesEndpoint import ProjectTicketsIdAllNotesEndpoint
from pywise.endpoints.manage.ProjectTicketsIdConfigurationsEndpoint import ProjectTicketsIdConfigurationsEndpoint
from pywise.endpoints.manage.ProjectTicketsIdConvertEndpoint import ProjectTicketsIdConvertEndpoint
from pywise.endpoints.manage.ProjectTicketsIdDocumentsEndpoint import ProjectTicketsIdDocumentsEndpoint
from pywise.endpoints.manage.ProjectTicketsIdNotesEndpoint import ProjectTicketsIdNotesEndpoint
from pywise.endpoints.manage.ProjectTicketsIdProductsEndpoint import ProjectTicketsIdProductsEndpoint
from pywise.endpoints.manage.ProjectTicketsIdScheduleentriesEndpoint import ProjectTicketsIdScheduleentriesEndpoint
from pywise.endpoints.manage.ProjectTicketsIdTasksEndpoint import ProjectTicketsIdTasksEndpoint
from pywise.endpoints.manage.ProjectTicketsIdTimeentriesEndpoint import ProjectTicketsIdTimeentriesEndpoint
from pywise.models.manage.ProjectTicketModel import ProjectTicketModel

class ProjectTicketsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
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
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectTicketModel]:
        """
        Performs a GET request against the /project/tickets/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTicketModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectTicketModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTicketModel:
        """
        Performs a GET request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicketModel: The parsed response data.
        """
        return self._parse_one(ProjectTicketModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTicketModel:
        """
        Performs a PUT request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicketModel: The parsed response data.
        """
        return self._parse_one(ProjectTicketModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTicketModel:
        """
        Performs a PATCH request against the /project/tickets/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTicketModel: The parsed response data.
        """
        return self._parse_one(ProjectTicketModel, super().make_request("PATCH", params=params).json())
        