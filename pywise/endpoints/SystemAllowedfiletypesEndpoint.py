from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.AllowedFileTypeModel import AllowedFileTypeModel

class SystemAllowedFileTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AllowedFileTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AllowedFileTypeModel,
            self,
            page_size,
        )
    
    def post(self, data=None, params=None) -> AllowedFileTypeModel:
        return self._parse_one(AllowedFileTypeModel, super().make_request("POST", params=params))
        