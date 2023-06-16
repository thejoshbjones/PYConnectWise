from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceEmailTemplatesIdEndpoint import ServiceEmailTemplatesIdEndpoint
from pywise.endpoints.ServiceEmailTemplatesCountEndpoint import ServiceEmailTemplatesCountEndpoint
from pywise.models.ServiceEmailTemplateModel import ServiceEmailTemplateModel

class ServiceEmailTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceEmailTemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceEmailTemplatesIdEndpoint:
        child = ServiceEmailTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceEmailTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceEmailTemplateModel]:
        return self._parse_many(ServiceEmailTemplateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceEmailTemplateModel:
        return self._parse_one(ServiceEmailTemplateModel, super().make_request("POST", params=params))
        