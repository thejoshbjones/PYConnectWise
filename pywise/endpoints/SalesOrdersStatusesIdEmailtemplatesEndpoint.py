from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOrdersStatusesIdEmailtemplatesIdEndpoint import SalesOrdersStatusesIdEmailtemplatesIdEndpoint
from pywise.endpoints.SalesOrdersStatusesIdEmailtemplatesCountEndpoint import SalesOrdersStatusesIdEmailtemplatesCountEndpoint
from pywise.models.OrderStatusEmailTemplateModel import OrderStatusEmailTemplateModel

class SalesOrdersStatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersStatusesIdEmailtemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOrdersStatusesIdEmailtemplatesIdEndpoint:
        child = SalesOrdersStatusesIdEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OrderStatusEmailTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OrderStatusEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OrderStatusEmailTemplateModel]:
        return self._parse_many(OrderStatusEmailTemplateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OrderStatusEmailTemplateModel:
        return self._parse_one(OrderStatusEmailTemplateModel, super().make_request("POST", params=params))
        