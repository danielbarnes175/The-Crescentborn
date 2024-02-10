label lovers_folly_main:
    scene bg lovers_folly with fade
    $ mc.location = Location.LOVERS_FOLLY
    "Welcome to Lover's Folly"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return