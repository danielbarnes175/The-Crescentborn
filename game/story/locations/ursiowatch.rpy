label ursiowatch_main:
    scene bg ursiowatch with fade
    $ mc_location = Location.URSIOWATCH
    "Welcome to Ursiowatch"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)
    
    return