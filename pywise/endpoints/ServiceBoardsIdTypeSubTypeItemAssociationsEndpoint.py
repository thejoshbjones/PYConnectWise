from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdTypeSubTypeItemAssociationsIdEndpoint import ServiceBoardsIdTypeSubTypeItemAssociationsIdEndpoint
from pywise.endpoints.ServiceBoardsIdTypeSubTypeItemAssociationsCountEndpoint import ServiceBoardsIdTypeSubTypeItemAssociationsCountEndpoint
from pywise.models.BoardTypeSubTypeItemAssociationModel import BoardTypeSubTypeItemAssociationModel

class ServiceBoardsIdTypeSubTypeItemAssociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "typeSubTypeItemAssociations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdTypeSubTypeItemAssociationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdTypeSubTypeItemAssociationsIdEndpoint:
        child = ServiceBoardsIdTypeSubTypeItemAssociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardTypeSubTypeItemAssociationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardTypeSubTypeItemAssociationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardTypeSubTypeItemAssociationModel]:
        return self._parse_many(BoardTypeSubTypeItemAssociationModel, super().make_request("GET", params=params))
        