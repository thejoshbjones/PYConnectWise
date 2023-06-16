from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdSitesIdEndpoint import FinanceAgreementsIdSitesIdEndpoint
from pywise.endpoints.FinanceAgreementsIdSitesCountEndpoint import FinanceAgreementsIdSitesCountEndpoint
from pywise.models.AgreementSiteModel import AgreementSiteModel

class FinanceAgreementsIdSitesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sites", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdSitesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdSitesIdEndpoint:
        child = FinanceAgreementsIdSitesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementSiteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementSiteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementSiteModel]:
        return self._parse_many(AgreementSiteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AgreementSiteModel:
        return self._parse_one(AgreementSiteModel, super().make_request("POST", params=params))
        