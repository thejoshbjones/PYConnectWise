from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMycompanyServicesIdEndpoint import SystemMycompanyServicesIdEndpoint
from pywise.models.ServiceModel import ServiceModel

class SystemMycompanyServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "services", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemMycompanyServicesIdEndpoint:
        child = SystemMycompanyServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceModel]:
        return self._parse_many(ServiceModel, super().make_request("GET", params=params))
        