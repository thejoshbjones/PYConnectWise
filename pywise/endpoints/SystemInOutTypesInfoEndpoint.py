from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.InOutTypeInfoModel import InOutTypeInfoModel

class SystemInOutTypesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InOutTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InOutTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InOutTypeInfoModel]:
        return self._parse_many(InOutTypeInfoModel, super().make_request("GET", params=params))
        