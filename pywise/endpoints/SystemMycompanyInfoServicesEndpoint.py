from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMycompanyInfoServicesIdEndpoint import SystemMycompanyInfoServicesIdEndpoint
from pywise.models.ServiceInfoModel import ServiceInfoModel

class SystemMycompanyInfoServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "services", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemMycompanyInfoServicesIdEndpoint:
        child = SystemMycompanyInfoServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceInfoModel]:
        return self._parse_many(ServiceInfoModel, super().make_request("GET", params=params))
        