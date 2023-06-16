from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdItemsIdAssociationsIdEndpoint import ServiceBoardsIdItemsIdAssociationsIdEndpoint
from pywise.endpoints.ServiceBoardsIdItemsIdAssociationsCountEndpoint import ServiceBoardsIdItemsIdAssociationsCountEndpoint
from pywise.models.BoardItemAssociationModel import BoardItemAssociationModel

class ServiceBoardsIdItemsIdAssociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "associations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdItemsIdAssociationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdItemsIdAssociationsIdEndpoint:
        child = ServiceBoardsIdItemsIdAssociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardItemAssociationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardItemAssociationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardItemAssociationModel]:
        return self._parse_many(BoardItemAssociationModel, super().make_request("GET", params=params))
        