from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOrdersStatusesIdNotificationsIdEndpoint import SalesOrdersStatusesIdNotificationsIdEndpoint
from pywise.endpoints.SalesOrdersStatusesIdNotificationsCountEndpoint import SalesOrdersStatusesIdNotificationsCountEndpoint
from pywise.models.OrderStatusNotificationModel import OrderStatusNotificationModel

class SalesOrdersStatusesIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersStatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOrdersStatusesIdNotificationsIdEndpoint:
        child = SalesOrdersStatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OrderStatusNotificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OrderStatusNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OrderStatusNotificationModel]:
        return self._parse_many(OrderStatusNotificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OrderStatusNotificationModel:
        return self._parse_one(OrderStatusNotificationModel, super().make_request("POST", params=params))
        