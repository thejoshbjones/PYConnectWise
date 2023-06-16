from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.BulkResultModel import BulkResultModel

class SystemMembersIdManagedDeviceAccountsBulkEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bulk", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BulkResultModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BulkResultModel,
            self,
            page_size,
        )
    
    def delete(self, data=None, params=None) -> BulkResultModel:
        return self._parse_one(BulkResultModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> BulkResultModel:
        return self._parse_one(BulkResultModel, super().make_request("PUT", params=params))
        