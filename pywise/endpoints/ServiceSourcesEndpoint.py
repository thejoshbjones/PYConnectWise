from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSourcesIdEndpoint import ServiceSourcesIdEndpoint
from pywise.endpoints.ServiceSourcesCountEndpoint import ServiceSourcesCountEndpoint
from pywise.endpoints.ServiceSourcesInfoEndpoint import ServiceSourcesInfoEndpoint
from pywise.models.SourceModel import SourceModel

class ServiceSourcesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sources", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSourcesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceSourcesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSourcesIdEndpoint:
        child = ServiceSourcesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SourceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SourceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SourceModel]:
        return self._parse_many(SourceModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SourceModel:
        return self._parse_one(SourceModel, super().make_request("POST", params=params))
        