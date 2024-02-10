label lilywatch_main:
    scene bg lilywatch with fade
    $ mc.location = Location.LILYWATCH
    "Welcome to Lilywatch"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return