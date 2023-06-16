from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsTypesIdEndpoint import FinanceAgreementsTypesIdEndpoint
from pywise.endpoints.FinanceAgreementsTypesCountEndpoint import FinanceAgreementsTypesCountEndpoint
from pywise.endpoints.FinanceAgreementsTypesInfoEndpoint import FinanceAgreementsTypesInfoEndpoint
from pywise.models.AgreementTypeModel import AgreementTypeModel

class FinanceAgreementsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceAgreementsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsTypesIdEndpoint:
        child = FinanceAgreementsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementTypeModel]:
        return self._parse_many(AgreementTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementTypeModel:
        return self._parse_one(AgreementTypeModel, super().make_request("POST", params=params))
        