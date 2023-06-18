from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceBoardsIdUsagesEndpoint import ServiceBoardsIdUsagesEndpoint
from pywise.endpoints.manage.ServiceBoardsIdAutoAssignResourcesEndpoint import ServiceBoardsIdAutoAssignResourcesEndpoint
from pywise.endpoints.manage.ServiceBoardsIdAutoTemplatesEndpoint import ServiceBoardsIdAutoTemplatesEndpoint
from pywise.endpoints.manage.ServiceBoardsIdExcludedMembersEndpoint import ServiceBoardsIdExcludedMembersEndpoint
from pywise.endpoints.manage.ServiceBoardsIdItemsEndpoint import ServiceBoardsIdItemsEndpoint
from pywise.endpoints.manage.ServiceBoardsIdNotificationsEndpoint import ServiceBoardsIdNotificationsEndpoint
from pywise.endpoints.manage.ServiceBoardsIdStatusesEndpoint import ServiceBoardsIdStatusesEndpoint
from pywise.endpoints.manage.ServiceBoardsIdSubtypesEndpoint import ServiceBoardsIdSubtypesEndpoint
from pywise.endpoints.manage.ServiceBoardsIdTeamsEndpoint import ServiceBoardsIdTeamsEndpoint
from pywise.endpoints.manage.ServiceBoardsIdTypesEndpoint import ServiceBoardsIdTypesEndpoint
from pywise.endpoints.manage.ServiceBoardsIdTypeSubTypeItemAssociationsEndpoint import ServiceBoardsIdTypeSubTypeItemAssociationsEndpoint
from pywise.models.manage.BoardModel import BoardModel

class ServiceBoardsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.usages = self.register_child_endpoint(
            ServiceBoardsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.autoAssignResources = self.register_child_endpoint(
            ServiceBoardsIdAutoAssignResourcesEndpoint(client, parent_endpoint=self)
        )
        self.autoTemplates = self.register_child_endpoint(
            ServiceBoardsIdAutoTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.excludedMembers = self.register_child_endpoint(
            ServiceBoardsIdExcludedMembersEndpoint(client, parent_endpoint=self)
        )
        self.items = self.register_child_endpoint(
            ServiceBoardsIdItemsEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self.register_child_endpoint(
            ServiceBoardsIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            ServiceBoardsIdStatusesEndpoint(client, parent_endpoint=self)
        )
        self.subtypes = self.register_child_endpoint(
            ServiceBoardsIdSubtypesEndpoint(client, parent_endpoint=self)
        )
        self.teams = self.register_child_endpoint(
            ServiceBoardsIdTeamsEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ServiceBoardsIdTypesEndpoint(client, parent_endpoint=self)
        )
        self.typeSubTypeItemAssociations = self.register_child_endpoint(
            ServiceBoardsIdTypeSubTypeItemAssociationsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardModel:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardModel: The parsed response data.
        """
        return self._parse_one(BoardModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardModel:
        """
        Performs a PUT request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardModel: The parsed response data.
        """
        return self._parse_one(BoardModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardModel:
        """
        Performs a PATCH request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardModel: The parsed response data.
        """
        return self._parse_one(BoardModel, super().make_request("PATCH", params=params).json())
        