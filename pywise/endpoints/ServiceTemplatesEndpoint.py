from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTemplatesIdEndpoint import ServiceTemplatesIdEndpoint
from pywise.endpoints.ServiceTemplatesCountEndpoint import ServiceTemplatesCountEndpoint
from pywise.endpoints.ServiceTemplatesInfoEndpoint import ServiceTemplatesInfoEndpoint
from pywise.models.ServiceTemplateModel import ServiceTemplateModel

class ServiceTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "templates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTemplatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTemplatesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTemplatesIdEndpoint:
        child = ServiceTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceTemplateModel]:
        return self._parse_many(ServiceTemplateModel, super().make_request("GET", params=params))
        