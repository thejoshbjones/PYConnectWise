from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdBoardDefaultsIdEndpoint import FinanceAgreementsIdBoardDefaultsIdEndpoint
from pywise.endpoints.FinanceAgreementsIdBoardDefaultsCountEndpoint import FinanceAgreementsIdBoardDefaultsCountEndpoint
from pywise.models.BoardDefaultModel import BoardDefaultModel

class FinanceAgreementsIdBoardDefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardDefaults", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdBoardDefaultsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdBoardDefaultsIdEndpoint:
        child = FinanceAgreementsIdBoardDefaultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardDefaultModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardDefaultModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardDefaultModel]:
        return self._parse_many(BoardDefaultModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardDefaultModel:
        return self._parse_one(BoardDefaultModel, super().make_request("POST", params=params))
        