label ursiowatch_main:
    scene bg ursiowatch with fade
    $ mc.location = Location.URSIOWATCH
    "Welcome to Ursiowatch"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return