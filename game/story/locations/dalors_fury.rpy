label dalors_fury_main:
    scene bg dalors_fury with fade
    $ mc.location = Location.DALORS_FURY
    "Welcome to Dalor's Fury"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return