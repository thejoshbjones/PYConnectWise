from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.CompanyFinanceModel import CompanyFinanceModel

class CompanyCompanyFinanceIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyFinanceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyFinanceModel,
            self,
            page_size,
        )
    
    def put(self, data=None, params=None) -> CompanyFinanceModel:
        return self._parse_one(CompanyFinanceModel, super().make_request("PUT", params=params))
        