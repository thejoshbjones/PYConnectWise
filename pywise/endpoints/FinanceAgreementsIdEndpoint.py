from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdAdditionsEndpoint import FinanceAgreementsIdAdditionsEndpoint
from pywise.endpoints.FinanceAgreementsIdAdjustmentsEndpoint import FinanceAgreementsIdAdjustmentsEndpoint
from pywise.endpoints.FinanceAgreementsIdBoardDefaultsEndpoint import FinanceAgreementsIdBoardDefaultsEndpoint
from pywise.endpoints.FinanceAgreementsIdConfigurationsEndpoint import FinanceAgreementsIdConfigurationsEndpoint
from pywise.endpoints.FinanceAgreementsIdSitesEndpoint import FinanceAgreementsIdSitesEndpoint
from pywise.endpoints.FinanceAgreementsIdWorkRoleExclusionsEndpoint import FinanceAgreementsIdWorkRoleExclusionsEndpoint
from pywise.endpoints.FinanceAgreementsIdWorkrolesEndpoint import FinanceAgreementsIdWorkrolesEndpoint
from pywise.endpoints.FinanceAgreementsIdWorkTypeExclusionsEndpoint import FinanceAgreementsIdWorkTypeExclusionsEndpoint
from pywise.endpoints.FinanceAgreementsIdWorktypesEndpoint import FinanceAgreementsIdWorktypesEndpoint
from pywise.models.AgreementModel import AgreementModel

class FinanceAgreementsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.additions = self.register_child_endpoint(
            FinanceAgreementsIdAdditionsEndpoint(client, parent_endpoint=self)
        )
        self.adjustments = self.register_child_endpoint(
            FinanceAgreementsIdAdjustmentsEndpoint(client, parent_endpoint=self)
        )
        self.boardDefaults = self.register_child_endpoint(
            FinanceAgreementsIdBoardDefaultsEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self.register_child_endpoint(
            FinanceAgreementsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.sites = self.register_child_endpoint(
            FinanceAgreementsIdSitesEndpoint(client, parent_endpoint=self)
        )
        self.workRoleExclusions = self.register_child_endpoint(
            FinanceAgreementsIdWorkRoleExclusionsEndpoint(client, parent_endpoint=self)
        )
        self.workroles = self.register_child_endpoint(
            FinanceAgreementsIdWorkrolesEndpoint(client, parent_endpoint=self)
        )
        self.workTypeExclusions = self.register_child_endpoint(
            FinanceAgreementsIdWorkTypeExclusionsEndpoint(client, parent_endpoint=self)
        )
        self.worktypes = self.register_child_endpoint(
            FinanceAgreementsIdWorktypesEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> AgreementModel:
        return self._parse_one(AgreementModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> AgreementModel:
        return self._parse_one(AgreementModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> AgreementModel:
        return self._parse_one(AgreementModel, super().make_request("PATCH", params=params))
        