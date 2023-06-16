from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.ScheduleCalendarsEndpoint import ScheduleCalendarsEndpoint
from pywise.endpoints.ScheduleColorsEndpoint import ScheduleColorsEndpoint
from pywise.endpoints.ScheduleDetailsEndpoint import ScheduleDetailsEndpoint
from pywise.endpoints.ScheduleEntriesEndpoint import ScheduleEntriesEndpoint
from pywise.endpoints.ScheduleHolidayListsEndpoint import ScheduleHolidayListsEndpoint
from pywise.endpoints.SchedulePortalcalendarsEndpoint import SchedulePortalcalendarsEndpoint
from pywise.endpoints.ScheduleReminderTimesEndpoint import ScheduleReminderTimesEndpoint
from pywise.endpoints.ScheduleStatusesEndpoint import ScheduleStatusesEndpoint
from pywise.endpoints.ScheduleTypesEndpoint import ScheduleTypesEndpoint

class ScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "schedule")
        
        self.calendars = self.register_child_endpoint(
            ScheduleCalendarsEndpoint(client, parent_endpoint=self)
        )
        self.colors = self.register_child_endpoint(
            ScheduleColorsEndpoint(client, parent_endpoint=self)
        )
        self.details = self.register_child_endpoint(
            ScheduleDetailsEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            ScheduleEntriesEndpoint(client, parent_endpoint=self)
        )
        self.holidayLists = self.register_child_endpoint(
            ScheduleHolidayListsEndpoint(client, parent_endpoint=self)
        )
        self.portalcalendars = self.register_child_endpoint(
            SchedulePortalcalendarsEndpoint(client, parent_endpoint=self)
        )
        self.reminderTimes = self.register_child_endpoint(
            ScheduleReminderTimesEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            ScheduleStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ScheduleTypesEndpoint(client, parent_endpoint=self)
        )