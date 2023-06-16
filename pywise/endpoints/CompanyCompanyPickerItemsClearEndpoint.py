from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.ClearPickerRequestModel import ClearPickerRequestModel

class CompanyCompanyPickerItemsClearEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "clear", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ClearPickerRequestModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ClearPickerRequestModel,
            self,
            page_size,
        )
    
    def post(self, data=None, params=None) -> ClearPickerRequestModel:
        return self._parse_one(ClearPickerRequestModel, super().make_request("POST", params=params))
        