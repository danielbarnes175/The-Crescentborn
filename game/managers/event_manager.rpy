init 1 python:
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
            #print(event.name, event.scene_triggered)
            if is_event_triggered(event.name) and not event.repeatable:
                continue  # Skip this event if already triggered

            if (week_number > event.week or (week_number == event.week and day_number >= event.day)):
                if ((time_of_day == event.time or event.time == Time.ANY) and mc_location == event.location):
                    prerequisites_met = check_prerequisites(event)
                    if prerequisites_met:
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
        return getattr(renpy.store, event_name).triggered

    # Define main storyline events
    main_story_events = {
        "generic_school_day": MainStoryEvent(name="generic_school_day", passage_name="generic_school_day", repeatable=True, week=1, day=1, time=Time.MORNING, location=Location.CLASSROOM),
        "scene_00_prologue": MainStoryEvent(name="scene_00_prologue", passage_name="scene_00_prologue", repeatable=False, week=1, day=1, time=Time.ANY, location=Location.UNKNOWN),
        "scene_01_first_day": MainStoryEvent(name="scene_01_first_day", passage_name="scene_01_first_day", repeatable=False, week=1, day=1, time=Time.MORNING, location=Location.DREAM),
        "second_dream": MainStoryEvent(name="second_dream", passage_name="second_dream", repeatable=False, week=1, day=4, time=Time.MORNING, location=Location.DORM),
        "balvor_tower_exploration": MainStoryEvent(name="balvor_tower_exploration", passage_name="balvor_tower_exploration", repeatable=False, week=2, day=1, time=Time.ANY, location=Location.BALVOR_TOWER)
        # Add more main storyline events here
    }

    # Define character events
    character_events = {
        # Bluejay
        "bluejay_intro": CharacterEvent(name="bluejay_intro", passage_name="bluejay_intro", repeatable=False, week=1, day=1, time=Time.MIDDAY, location=Location.PRAELOR, relationship_threshold=0),
        "bluejay_generic_hangout": CharacterEvent(name="bluejay_generic_hangout", passage_name="bluejay_generic_hangout", repeatable=True, week=1, day=1, time=Time.ANY, location=Location.PRAELOR_BRASHY_BREW, relationship_threshold=0, prerequisites=["bluejay_intro"]),

        # Gudrak
        "gudrak_intro": CharacterEvent(name="gudrak_intro", passage_name="gudrak_intro", repeatable=False, week=1, day=1, time=Time.MIDDAY, location=Location.THE_CITADEL_LIBRARY, relationship_threshold=0),
        "gudrak_generic_hangout": CharacterEvent(name="gudrak_generic_hangout", passage_name="gudrak_generic_hangout", repeatable=True, week=1, day=1, time=Time.ANY, location=Location.THE_CITADEL_LIBRARY, relationship_threshold=0, prerequisites=["gudrak_intro"]),

        # Kuviis
        "kuviis_intro": CharacterEvent(name="kuviis_intro", passage_name="kuviis_intro", repeatable=False, week=1, day=1, time=Time.MIDDAY, location=Location.LOVERS_FOLLY, relationship_threshold=0),
        "kuviis_generic_hangout": CharacterEvent(name="kuviis_generic_hangout", passage_name="kuviis_generic_hangout", repeatable=True, week=1, day=1, time=Time.ANY, location=Location.LOVERS_FOLLY, relationship_threshold=0, prerequisites=["kuviis_intro"]),
        
        # Ralph
        "ralph_intro": CharacterEvent(name="ralph_intro", passage_name="ralph_intro", repeatable=False, week=1, day=1, time=Time.MIDDAY, location=Location.FIGHTERS_GUILD, relationship_threshold=0),
        "ralph_generic_hangout": CharacterEvent(name="ralph_generic_hangout", passage_name="ralph_generic_hangout", repeatable=True, week=1, day=1, time=Time.ANY, location=Location.FIGHTERS_GUILD, relationship_threshold=0, prerequisites=["ralph_intro"]),

        # Add more character events here
    }