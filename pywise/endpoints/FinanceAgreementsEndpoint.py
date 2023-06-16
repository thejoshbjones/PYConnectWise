from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdEndpoint import FinanceAgreementsIdEndpoint
from pywise.endpoints.FinanceAgreementsCountEndpoint import FinanceAgreementsCountEndpoint
from pywise.endpoints.FinanceAgreementsTypesEndpoint import FinanceAgreementsTypesEndpoint
from pywise.models.AgreementModel import AgreementModel

class FinanceAgreementsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "agreements", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            FinanceAgreementsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdEndpoint:
        child = FinanceAgreementsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementModel]:
        return self._parse_many(AgreementModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementModel:
        return self._parse_one(AgreementModel, super().make_request("POST", params=params))
        