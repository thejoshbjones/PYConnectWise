from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoLocalesIdEndpoint import SystemInfoLocalesIdEndpoint
from pywise.endpoints.SystemInfoLocalesCountEndpoint import SystemInfoLocalesCountEndpoint
from pywise.models.LocaleInfoModel import LocaleInfoModel

class SystemInfoLocalesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locales", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoLocalesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoLocalesIdEndpoint:
        child = SystemInfoLocalesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LocaleInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LocaleInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LocaleInfoModel]:
        return self._parse_many(LocaleInfoModel, super().make_request("GET", params=params))
        