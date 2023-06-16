from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOrdersStatusesIdEndpoint import SalesOrdersStatusesIdEndpoint
from pywise.endpoints.SalesOrdersStatusesCountEndpoint import SalesOrdersStatusesCountEndpoint
from pywise.endpoints.SalesOrdersStatusesInfoEndpoint import SalesOrdersStatusesInfoEndpoint
from pywise.models.OrderStatusModel import OrderStatusModel

class SalesOrdersStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOrdersStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOrdersStatusesIdEndpoint:
        child = SalesOrdersStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OrderStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OrderStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OrderStatusModel]:
        return self._parse_many(OrderStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> list[OrderStatusModel]:
        return self._parse_many(OrderStatusModel, super().make_request("POST", params=params))
        