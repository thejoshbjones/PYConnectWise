from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdWorkRoleExclusionsIdEndpoint import FinanceAgreementsIdWorkRoleExclusionsIdEndpoint
from pywise.endpoints.FinanceAgreementsIdWorkRoleExclusionsCountEndpoint import FinanceAgreementsIdWorkRoleExclusionsCountEndpoint
from pywise.models.AgreementWorkRoleExclusionModel import AgreementWorkRoleExclusionModel

class FinanceAgreementsIdWorkRoleExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorkRoleExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdWorkRoleExclusionsIdEndpoint:
        child = FinanceAgreementsIdWorkRoleExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementWorkRoleExclusionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementWorkRoleExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementWorkRoleExclusionModel]:
        return self._parse_many(AgreementWorkRoleExclusionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementWorkRoleExclusionModel:
        return self._parse_one(AgreementWorkRoleExclusionModel, super().make_request("POST", params=params))
        