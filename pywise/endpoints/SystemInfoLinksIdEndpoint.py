from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoLinksIdResolveurlEndpoint import SystemInfoLinksIdResolveurlEndpoint
from pywise.models.LinkInfoModel import LinkInfoModel

class SystemInfoLinksIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.resolveurl = self.register_child_endpoint(
            SystemInfoLinksIdResolveurlEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> LinkInfoModel:
        return self._parse_one(LinkInfoModel, super().make_request("GET", params=params))
        