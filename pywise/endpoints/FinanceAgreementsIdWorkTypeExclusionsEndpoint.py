from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdWorkTypeExclusionsIdEndpoint import FinanceAgreementsIdWorkTypeExclusionsIdEndpoint
from pywise.endpoints.FinanceAgreementsIdWorkTypeExclusionsCountEndpoint import FinanceAgreementsIdWorkTypeExclusionsCountEndpoint
from pywise.models.AgreementWorkTypeExclusionModel import AgreementWorkTypeExclusionModel

class FinanceAgreementsIdWorkTypeExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workTypeExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorkTypeExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdWorkTypeExclusionsIdEndpoint:
        child = FinanceAgreementsIdWorkTypeExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementWorkTypeExclusionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementWorkTypeExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementWorkTypeExclusionModel]:
        return self._parse_many(AgreementWorkTypeExclusionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementWorkTypeExclusionModel:
        return self._parse_one(AgreementWorkTypeExclusionModel, super().make_request("POST", params=params))
        