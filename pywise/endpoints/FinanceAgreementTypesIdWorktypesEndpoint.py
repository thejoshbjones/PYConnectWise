from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementTypesIdWorktypesIdEndpoint import FinanceAgreementTypesIdWorktypesIdEndpoint
from pywise.endpoints.FinanceAgreementTypesIdWorktypesCountEndpoint import FinanceAgreementTypesIdWorktypesCountEndpoint
from pywise.models.AgreementTypeWorkTypeModel import AgreementTypeWorkTypeModel

class FinanceAgreementTypesIdWorktypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "worktypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorktypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorktypesIdEndpoint:
        child = FinanceAgreementTypesIdWorktypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeWorkTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeWorkTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeWorkTypeModel]:
        return self._parse_many(AgreementTypeWorkTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementTypeWorkTypeModel:
        return self._parse_one(AgreementTypeWorkTypeModel, super().make_request("POST", params=params))
        