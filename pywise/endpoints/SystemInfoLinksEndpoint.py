from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoLinksIdEndpoint import SystemInfoLinksIdEndpoint
from pywise.endpoints.SystemInfoLinksCountEndpoint import SystemInfoLinksCountEndpoint
from pywise.models.LinkInfoModel import LinkInfoModel

class SystemInfoLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "links", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoLinksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoLinksIdEndpoint:
        child = SystemInfoLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LinkInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LinkInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LinkInfoModel]:
        return self._parse_many(LinkInfoModel, super().make_request("GET", params=params))
        