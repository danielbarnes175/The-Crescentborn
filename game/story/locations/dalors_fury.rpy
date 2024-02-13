label dalors_fury_main:
    scene bg dalors_fury with fade
    $ mc_location = Location.DALORS_FURY
    "Welcome to Dalor's Fury"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)
    
    return