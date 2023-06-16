from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceGlAccountsIdEndpoint import FinanceGlAccountsIdEndpoint
from pywise.endpoints.FinanceGlAccountsCountEndpoint import FinanceGlAccountsCountEndpoint
from pywise.endpoints.FinanceGlAccountsMappedTypesEndpoint import FinanceGlAccountsMappedTypesEndpoint
from pywise.models.GLAccountModel import GLAccountModel

class FinanceGlAccountsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glAccounts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlAccountsCountEndpoint(client, parent_endpoint=self)
        )
        self.mappedTypes = self.register_child_endpoint(
            FinanceGlAccountsMappedTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceGlAccountsIdEndpoint:
        child = FinanceGlAccountsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[GLAccountModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            GLAccountModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[GLAccountModel]:
        return self._parse_many(GLAccountModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> GLAccountModel:
        return self._parse_one(GLAccountModel, super().make_request("POST", params=params))
        