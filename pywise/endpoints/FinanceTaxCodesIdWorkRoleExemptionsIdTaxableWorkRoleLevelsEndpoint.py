from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint import FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsCountEndpoint import FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsCountEndpoint
from pywise.models.TaxableWorkRoleLevelModel import TaxableWorkRoleLevelModel

class FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableWorkRoleLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint:
        child = FinanceTaxCodesIdWorkRoleExemptionsIdTaxableWorkRoleLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxableWorkRoleLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxableWorkRoleLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxableWorkRoleLevelModel]:
        return self._parse_many(TaxableWorkRoleLevelModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxableWorkRoleLevelModel:
        return self._parse_one(TaxableWorkRoleLevelModel, super().make_request("POST", params=params))
        