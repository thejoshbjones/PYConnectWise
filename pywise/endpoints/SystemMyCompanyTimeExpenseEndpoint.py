from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyCompanyTimeExpenseIdEndpoint import SystemMyCompanyTimeExpenseIdEndpoint
from pywise.endpoints.SystemMyCompanyTimeExpenseCountEndpoint import SystemMyCompanyTimeExpenseCountEndpoint
from pywise.models.TimeExpenseModel import TimeExpenseModel

class SystemMyCompanyTimeExpenseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeExpense", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyTimeExpenseCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMyCompanyTimeExpenseIdEndpoint:
        child = SystemMyCompanyTimeExpenseIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeExpenseModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeExpenseModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeExpenseModel]:
        return self._parse_many(TimeExpenseModel, super().make_request("GET", params=params))
        