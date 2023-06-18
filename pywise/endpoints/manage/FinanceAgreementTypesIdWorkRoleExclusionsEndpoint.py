from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint import FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint
from pywise.endpoints.manage.FinanceAgreementTypesIdWorkRoleExclusionsCountEndpoint import FinanceAgreementTypesIdWorkRoleExclusionsCountEndpoint
from pywise.models.manage.AgreementTypeWorkRoleExclusionModel import AgreementTypeWorkRoleExclusionModel

class FinanceAgreementTypesIdWorkRoleExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoleExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkRoleExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint:
        child = FinanceAgreementTypesIdWorkRoleExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeWorkRoleExclusionModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workRoleExclusions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRoleExclusionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeWorkRoleExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkRoleExclusionModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRoleExclusionModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkRoleExclusionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkRoleExclusionModel:
        """
        Performs a POST request against the /finance/agreementTypes/{parentId}/workRoleExclusions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkRoleExclusionModel: The parsed response data.
        """
        return self._parse_one(AgreementTypeWorkRoleExclusionModel, super().make_request("POST", params=params).json())
        