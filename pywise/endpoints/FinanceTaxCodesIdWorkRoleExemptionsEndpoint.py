from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint import FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdWorkRoleExemptionsCountEndpoint import FinanceTaxCodesIdWorkRoleExemptionsCountEndpoint
from pywise.models.WorkRoleExemptionModel import WorkRoleExemptionModel

class FinanceTaxCodesIdWorkRoleExemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExemptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdWorkRoleExemptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint:
        child = FinanceTaxCodesIdWorkRoleExemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkRoleExemptionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkRoleExemptionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkRoleExemptionModel]:
        return self._parse_many(WorkRoleExemptionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkRoleExemptionModel:
        return self._parse_one(WorkRoleExemptionModel, super().make_request("POST", params=params))
        