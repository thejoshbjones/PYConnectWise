from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpenseTypesIdEndpoint import ExpenseTypesIdEndpoint
from pywise.endpoints.ExpenseTypesCountEndpoint import ExpenseTypesCountEndpoint
from pywise.endpoints.ExpenseTypesInfoEndpoint import ExpenseTypesInfoEndpoint
from pywise.models.ExpenseTypeModel import ExpenseTypeModel

class ExpenseTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ExpenseTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpenseTypesIdEndpoint:
        child = ExpenseTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExpenseTypeModel]:
        return self._parse_many(ExpenseTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ExpenseTypeModel:
        return self._parse_one(ExpenseTypeModel, super().make_request("POST", params=params))
        