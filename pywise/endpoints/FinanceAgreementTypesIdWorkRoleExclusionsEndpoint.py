from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint import FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint
from pywise.endpoints.FinanceAgreementTypesIdWorkRoleExclusionsCountEndpoint import FinanceAgreementTypesIdWorkRoleExclusionsCountEndpoint
from pywise.models.AgreementTypeWorkRoleExclusionModel import AgreementTypeWorkRoleExclusionModel

class FinanceAgreementTypesIdWorkRoleExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkRoleExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint:
        child = FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeWorkRoleExclusionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeWorkRoleExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeWorkRoleExclusionModel]:
        return self._parse_many(AgreementTypeWorkRoleExclusionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementTypeWorkRoleExclusionModel:
        return self._parse_one(AgreementTypeWorkRoleExclusionModel, super().make_request("POST", params=params))
        