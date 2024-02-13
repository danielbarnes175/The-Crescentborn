init 1 python:
    # from game.managers.time_manager import Time, DayOfWeek

    class MainStoryEvent:
        def __init__(self, name, passage_name, repeatable, week, day, time, location, prerequisites=None):
            self.name = name
            self.passage_name = passage_name
            self.repeatable = repeatable
            self.week = week
            self.day = day
            self.time = time
            self.location = location
            self.prerequisites = prerequisites if prerequisites else []
            self.scene_triggered = False

    class CharacterEvent:
        def __init__(self, name, passage_name, repeatable, week, day, time, location, relationship_threshold, prerequisites=None):
            self.name = name
            self.passage_name = passage_name
            self.repeatable = repeatable
            self.week = week
            self.day = day
            self.time = time
            self.location = location
            self.relationship_threshold = relationship_threshold
            self.prerequisites = prerequisites if prerequisites else []
            self.scene_triggered = False

    def trigger_events(events, event_type):
        # Loop through all events
        for key, event in events.items():
            print(event.name, event.scene_triggered)
            if event.scene_triggered and not event.repeatable:
                continue  # Skip this event if already triggered

            if (week_number > event.week or (week_number == event.week and day_number >= event.day)):
                if ((time_of_day == event.time or event.time == Time.ANY) and mc_location == event.location):
                    prerequisites_met = check_prerequisites(event)
                    if prerequisites_met:
                        # Trigger the event's scene
                        events[key].scene_triggered = True
                        renpy.call(event.passage_name)


    def check_prerequisites(event):
        prerequisites_met = True
        for prerequisite_name in event.prerequisites:
            is_prerequisite_triggered = is_event_triggered(prerequisite_name)
            if not is_prerequisite_triggered:
                prerequisites_met = False
                break
        return prerequisites_met

    def is_event_triggered(event_name):
        main_story_event = main_story_events.get(event_name)
        if main_story_event and main_story_event.scene_triggered:
            return True

        character_event = character_events.get(event_name)
        if character_event and character_event.scene_triggered:
            return True

        return False

    # Define main storyline events
    main_story_events = {
        "generic_school_day": MainStoryEvent(name="generic_school_day", passage_name="generic_school_day", repeatable=True, week=1, day=1, time=Time.MORNING, location=Location.CLASSROOM),
        # Add more main storyline events here
    }

    # Define character events
    character_events = {
        "kuviis_intro": CharacterEvent(name="kuviis_intro", passage_name="kuviis_intro", repeatable=False, week=1, day=1, time=Time.MIDDAY, location=Location.LOVERS_FOLLY, relationship_threshold=0),
        "kuviis_generic_hangout": CharacterEvent(name="kuviis_generic_hangout", passage_name="kuviis_generic_hangout", repeatable=True, week=1, day=1, time=Time.ANY, location=Location.LOVERS_FOLLY, relationship_threshold=0, prerequisites=["kuviis_intro"]),
        # Add more character events here
    }