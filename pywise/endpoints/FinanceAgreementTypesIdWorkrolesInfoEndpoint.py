from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementTypesIdWorkrolesInfoIdEndpoint import FinanceAgreementTypesIdWorkrolesInfoIdEndpoint
from pywise.endpoints.FinanceAgreementTypesIdWorkrolesInfoCountEndpoint import FinanceAgreementTypesIdWorkrolesInfoCountEndpoint
from pywise.models.AgreementTypeWorkRoleInfoModel import AgreementTypeWorkRoleInfoModel

class FinanceAgreementTypesIdWorkrolesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkrolesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkrolesInfoIdEndpoint:
        child = FinanceAgreementTypesIdWorkrolesInfoIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeWorkRoleInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeWorkRoleInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeWorkRoleInfoModel]:
        return self._parse_many(AgreementTypeWorkRoleInfoModel, super().make_request("GET", params=params))
        