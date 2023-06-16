from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdNotificationsIdEndpoint import ServiceBoardsIdNotificationsIdEndpoint
from pywise.endpoints.ServiceBoardsIdNotificationsCountEndpoint import ServiceBoardsIdNotificationsCountEndpoint
from pywise.models.BoardNotificationModel import BoardNotificationModel

class ServiceBoardsIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdNotificationsIdEndpoint:
        child = ServiceBoardsIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardNotificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardNotificationModel]:
        return self._parse_many(BoardNotificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardNotificationModel:
        return self._parse_one(BoardNotificationModel, super().make_request("POST", params=params))
        