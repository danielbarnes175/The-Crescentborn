label the_citadel_main:
    scene bg the_citadel with fade
    $ mc_location = Location.THE_CITADEL
    "You made your way over to The Citadel"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

    return