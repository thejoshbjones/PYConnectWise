from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementTypesIdBoardDefaultsIdEndpoint import FinanceAgreementTypesIdBoardDefaultsIdEndpoint
from pywise.endpoints.FinanceAgreementTypesIdBoardDefaultsCountEndpoint import FinanceAgreementTypesIdBoardDefaultsCountEndpoint
from pywise.models.AgreementTypeBoardDefaultModel import AgreementTypeBoardDefaultModel

class FinanceAgreementTypesIdBoardDefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardDefaults", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdBoardDefaultsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdBoardDefaultsIdEndpoint:
        child = FinanceAgreementTypesIdBoardDefaultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeBoardDefaultModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeBoardDefaultModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeBoardDefaultModel]:
        return self._parse_many(AgreementTypeBoardDefaultModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementTypeBoardDefaultModel:
        return self._parse_one(AgreementTypeBoardDefaultModel, super().make_request("POST", params=params))
        