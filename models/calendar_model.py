from ics import Calendar, Event
from datetime import datetime

class CalendarModel:
    def create_event(self, summary, description, start_time, end_time):
        try:
            calendar = Calendar()
            event = Event()

            event.name = summary
            event.description = description
            event.begin = start_time
            event.end = end_time

            calendar.events.add(event)
            
            # Save to .ics file
            file_name = "meeting_event.ics"
            with open(file_name, "w") as file:
                file.writelines(calendar)
            return file_name
        except Exception as e:
            return str(e)
