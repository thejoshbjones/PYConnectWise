from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTemplatesIdGenerateEndpoint import ServiceTemplatesIdGenerateEndpoint
from pywise.endpoints.ServiceTemplatesIdInfoEndpoint import ServiceTemplatesIdInfoEndpoint
from pywise.models.ServiceTemplateModel import ServiceTemplateModel

class ServiceTemplatesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.generate = self.register_child_endpoint(
            ServiceTemplatesIdGenerateEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTemplatesIdInfoEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> ServiceTemplateModel:
        return self._parse_one(ServiceTemplateModel, super().make_request("GET", params=params))
        