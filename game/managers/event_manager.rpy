init python:
    main_storyline_events_schedule = {
        1: {  # Week 1
            1: {  # Monday
                "morning": "Event A",
                "day": "Event B",
            },
            2: {  # Tuesday
                "evening": "Event F"
            },
            # ... continue for other days and times
        },
        # ... continue for other weeks
    }

    def get_event_by_time(week, day, time):
        try:
            event_name = main_storyline_events_schedule[week][day][time]
        except KeyError:
            event_name = ""  # Return empty string if no event found
            
        return event_name