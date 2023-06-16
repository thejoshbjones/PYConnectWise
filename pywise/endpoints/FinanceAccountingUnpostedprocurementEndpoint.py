from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedprocurementIdEndpoint import FinanceAccountingUnpostedprocurementIdEndpoint
from pywise.endpoints.FinanceAccountingUnpostedprocurementCountEndpoint import FinanceAccountingUnpostedprocurementCountEndpoint
from pywise.models.UnpostedProcurementModel import UnpostedProcurementModel

class FinanceAccountingUnpostedprocurementEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unpostedprocurement", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedprocurementCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingUnpostedprocurementIdEndpoint:
        child = FinanceAccountingUnpostedprocurementIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnpostedProcurementModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnpostedProcurementModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnpostedProcurementModel]:
        return self._parse_many(UnpostedProcurementModel, super().make_request("GET", params=params))
        