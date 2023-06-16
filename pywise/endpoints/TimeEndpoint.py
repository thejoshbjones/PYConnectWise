from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.TimeAccrualsEndpoint import TimeAccrualsEndpoint
from pywise.endpoints.TimeActivitystopwatchesEndpoint import TimeActivitystopwatchesEndpoint
from pywise.endpoints.TimeChargeCodesEndpoint import TimeChargeCodesEndpoint
from pywise.endpoints.TimeEntriesEndpoint import TimeEntriesEndpoint
from pywise.endpoints.TimeSchedulestopwatchesEndpoint import TimeSchedulestopwatchesEndpoint
from pywise.endpoints.TimeSheetsEndpoint import TimeSheetsEndpoint
from pywise.endpoints.TimeTicketstopwatchesEndpoint import TimeTicketstopwatchesEndpoint
from pywise.endpoints.TimeTimePeriodSetupsEndpoint import TimeTimePeriodSetupsEndpoint
from pywise.endpoints.TimeWorkRolesEndpoint import TimeWorkRolesEndpoint
from pywise.endpoints.TimeWorkTypesEndpoint import TimeWorkTypesEndpoint

class TimeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "time")
        
        self.accruals = self.register_child_endpoint(
            TimeAccrualsEndpoint(client, parent_endpoint=self)
        )
        self.activitystopwatches = self.register_child_endpoint(
            TimeActivitystopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.chargeCodes = self.register_child_endpoint(
            TimeChargeCodesEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            TimeEntriesEndpoint(client, parent_endpoint=self)
        )
        self.schedulestopwatches = self.register_child_endpoint(
            TimeSchedulestopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.sheets = self.register_child_endpoint(
            TimeSheetsEndpoint(client, parent_endpoint=self)
        )
        self.ticketstopwatches = self.register_child_endpoint(
            TimeTicketstopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.timePeriodSetups = self.register_child_endpoint(
            TimeTimePeriodSetupsEndpoint(client, parent_endpoint=self)
        )
        self.workRoles = self.register_child_endpoint(
            TimeWorkRolesEndpoint(client, parent_endpoint=self)
        )
        self.workTypes = self.register_child_endpoint(
            TimeWorkTypesEndpoint(client, parent_endpoint=self)
        )