from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyCompanyOtherIdEndpoint import SystemMyCompanyOtherIdEndpoint
from pywise.endpoints.SystemMyCompanyOtherCountEndpoint import SystemMyCompanyOtherCountEndpoint
from pywise.models.OtherModel import OtherModel

class SystemMyCompanyOtherEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "other", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyOtherCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMyCompanyOtherIdEndpoint:
        child = SystemMyCompanyOtherIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OtherModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OtherModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OtherModel]:
        return self._parse_many(OtherModel, super().make_request("GET", params=params))
        