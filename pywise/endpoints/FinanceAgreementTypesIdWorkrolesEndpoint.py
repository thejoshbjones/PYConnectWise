from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementTypesIdWorkrolesIdEndpoint import FinanceAgreementTypesIdWorkrolesIdEndpoint
from pywise.endpoints.FinanceAgreementTypesIdWorkrolesCountEndpoint import FinanceAgreementTypesIdWorkrolesCountEndpoint
from pywise.endpoints.FinanceAgreementTypesIdWorkrolesInfoEndpoint import FinanceAgreementTypesIdWorkrolesInfoEndpoint
from pywise.models.AgreementTypeWorkRoleModel import AgreementTypeWorkRoleModel

class FinanceAgreementTypesIdWorkrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workroles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkrolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkrolesIdEndpoint:
        child = FinanceAgreementTypesIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeWorkRoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeWorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeWorkRoleModel]:
        return self._parse_many(AgreementTypeWorkRoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementTypeWorkRoleModel:
        return self._parse_one(AgreementTypeWorkRoleModel, super().make_request("POST", params=params))
        