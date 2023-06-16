from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint import FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint
from pywise.endpoints.FinanceAgreementTypesIdWorkTypeExclusionsCountEndpoint import FinanceAgreementTypesIdWorkTypeExclusionsCountEndpoint
from pywise.models.AgreementTypeWorkTypeExclusionModel import AgreementTypeWorkTypeExclusionModel

class FinanceAgreementTypesIdWorkTypeExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workTypeExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkTypeExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint:
        child = FinanceAgreementTypesIdWorkTypeExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeWorkTypeExclusionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeWorkTypeExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeWorkTypeExclusionModel]:
        return self._parse_many(AgreementTypeWorkTypeExclusionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementTypeWorkTypeExclusionModel:
        return self._parse_one(AgreementTypeWorkTypeExclusionModel, super().make_request("POST", params=params))
        