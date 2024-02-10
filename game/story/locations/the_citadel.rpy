label the_citadel_main:
    scene bg the_citadel with fade
    $ mc.location = Location.THE_CITADEL
    "Welcome to The Citadel"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return