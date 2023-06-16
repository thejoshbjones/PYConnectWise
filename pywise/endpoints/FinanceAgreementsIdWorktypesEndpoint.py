from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdWorktypesIdEndpoint import FinanceAgreementsIdWorktypesIdEndpoint
from pywise.endpoints.FinanceAgreementsIdWorktypesCountEndpoint import FinanceAgreementsIdWorktypesCountEndpoint
from pywise.models.AgreementWorkTypeModel import AgreementWorkTypeModel

class FinanceAgreementsIdWorktypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "worktypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorktypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdWorktypesIdEndpoint:
        child = FinanceAgreementsIdWorktypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementWorkTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementWorkTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementWorkTypeModel]:
        return self._parse_many(AgreementWorkTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementWorkTypeModel:
        return self._parse_one(AgreementWorkTypeModel, super().make_request("POST", params=params))
        