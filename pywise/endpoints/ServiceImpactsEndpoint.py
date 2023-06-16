from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceImpactsIdEndpoint import ServiceImpactsIdEndpoint
from pywise.endpoints.ServiceImpactsCountEndpoint import ServiceImpactsCountEndpoint
from pywise.models.ImpactModel import ImpactModel

class ServiceImpactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "impacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceImpactsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceImpactsIdEndpoint:
        child = ServiceImpactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ImpactModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ImpactModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ImpactModel]:
        return self._parse_many(ImpactModel, super().make_request("GET", params=params))
        