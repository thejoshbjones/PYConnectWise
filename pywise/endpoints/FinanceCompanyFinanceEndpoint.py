from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceCompanyFinanceIdEndpoint import FinanceCompanyFinanceIdEndpoint
from pywise.endpoints.FinanceCompanyFinanceCountEndpoint import FinanceCompanyFinanceCountEndpoint
from pywise.models.CompanyFinanceModel import CompanyFinanceModel

class FinanceCompanyFinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceCompanyFinanceCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceCompanyFinanceIdEndpoint:
        child = FinanceCompanyFinanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[CompanyFinanceModel]:
        return self._parse_many(CompanyFinanceModel, super().make_request("GET", params=params))
        