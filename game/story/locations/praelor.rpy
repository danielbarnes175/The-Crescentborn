label praelor_main:
    scene bg praelor with fade
    $ mc_location = Location.PRAELOR
    "You made your way over to Praelor"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

    return