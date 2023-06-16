from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdUsagesEndpoint import ServiceBoardsIdUsagesEndpoint
from pywise.endpoints.ServiceBoardsIdAutoAssignResourcesEndpoint import ServiceBoardsIdAutoAssignResourcesEndpoint
from pywise.endpoints.ServiceBoardsIdAutoTemplatesEndpoint import ServiceBoardsIdAutoTemplatesEndpoint
from pywise.endpoints.ServiceBoardsIdExcludedMembersEndpoint import ServiceBoardsIdExcludedMembersEndpoint
from pywise.endpoints.ServiceBoardsIdItemsEndpoint import ServiceBoardsIdItemsEndpoint
from pywise.endpoints.ServiceBoardsIdNotificationsEndpoint import ServiceBoardsIdNotificationsEndpoint
from pywise.endpoints.ServiceBoardsIdStatusesEndpoint import ServiceBoardsIdStatusesEndpoint
from pywise.endpoints.ServiceBoardsIdSubtypesEndpoint import ServiceBoardsIdSubtypesEndpoint
from pywise.endpoints.ServiceBoardsIdTeamsEndpoint import ServiceBoardsIdTeamsEndpoint
from pywise.endpoints.ServiceBoardsIdTypesEndpoint import ServiceBoardsIdTypesEndpoint
from pywise.endpoints.ServiceBoardsIdTypeSubTypeItemAssociationsEndpoint import ServiceBoardsIdTypeSubTypeItemAssociationsEndpoint
from pywise.models.BoardModel import BoardModel

class ServiceBoardsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> BoardModel:
        return self._parse_one(BoardModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> BoardModel:
        return self._parse_one(BoardModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> BoardModel:
        return self._parse_one(BoardModel, super().make_request("PATCH", params=params))
        