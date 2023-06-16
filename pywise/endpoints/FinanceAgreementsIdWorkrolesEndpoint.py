from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdWorkrolesIdEndpoint import FinanceAgreementsIdWorkrolesIdEndpoint
from pywise.endpoints.FinanceAgreementsIdWorkrolesCountEndpoint import FinanceAgreementsIdWorkrolesCountEndpoint
from pywise.models.AgreementWorkRoleModel import AgreementWorkRoleModel

class FinanceAgreementsIdWorkrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workroles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdWorkrolesIdEndpoint:
        child = FinanceAgreementsIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementWorkRoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementWorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementWorkRoleModel]:
        return self._parse_many(AgreementWorkRoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementWorkRoleModel:
        return self._parse_one(AgreementWorkRoleModel, super().make_request("POST", params=params))
        