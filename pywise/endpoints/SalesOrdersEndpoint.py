from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOrdersIdEndpoint import SalesOrdersIdEndpoint
from pywise.endpoints.SalesOrdersCountEndpoint import SalesOrdersCountEndpoint
from pywise.endpoints.SalesOrdersStatusesEndpoint import SalesOrdersStatusesEndpoint
from pywise.models.OrderModel import OrderModel

class SalesOrdersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "orders", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            SalesOrdersStatusesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOrdersIdEndpoint:
        child = SalesOrdersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OrderModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OrderModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OrderModel]:
        return self._parse_many(OrderModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OrderModel:
        return self._parse_one(OrderModel, super().make_request("POST", params=params))
        