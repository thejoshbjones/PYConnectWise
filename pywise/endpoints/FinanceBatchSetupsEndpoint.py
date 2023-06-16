from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceBatchSetupsIdEndpoint import FinanceBatchSetupsIdEndpoint
from pywise.endpoints.FinanceBatchSetupsCountEndpoint import FinanceBatchSetupsCountEndpoint
from pywise.models.AgreementBatchSetupModel import AgreementBatchSetupModel

class FinanceBatchSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "batchSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBatchSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceBatchSetupsIdEndpoint:
        child = FinanceBatchSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AgreementBatchSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AgreementBatchSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AgreementBatchSetupModel]:
        return self._parse_many(AgreementBatchSetupModel, super().make_request("GET", params=params))
        