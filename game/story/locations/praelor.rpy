label praelor_main:
    scene bg praelor with fade
    $ mc.location = Location.PRAELOR
    "Welcome to Praelor"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return