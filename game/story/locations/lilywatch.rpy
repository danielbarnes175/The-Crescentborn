label lilywatch_main:
    scene bg lilywatch with fade
    $ mc_location = Location.LILYWATCH
    "Welcome to Lilywatch"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)
    
    return