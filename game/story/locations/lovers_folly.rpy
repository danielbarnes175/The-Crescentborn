label lovers_folly_main:
    scene bg lovers_folly with fade
    $ mc_location = Location.LOVERS_FOLLY
    "You made your way over to Lover's Folly"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

