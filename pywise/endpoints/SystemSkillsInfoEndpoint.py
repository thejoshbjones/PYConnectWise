from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSkillsInfoCountEndpoint import SystemSkillsInfoCountEndpoint
from pywise.models.SkillInfoModel import SkillInfoModel

class SystemSkillsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSkillsInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SkillInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SkillInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SkillInfoModel]:
        return self._parse_many(SkillInfoModel, super().make_request("GET", params=params))
        