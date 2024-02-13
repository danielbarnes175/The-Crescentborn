label temple_of_aeyenlo_main:
    scene bg temple_of_aeyenlo with fade
    $ mc_location = Location.TEMPLE_OF_AEYENLO
    "You made your way over to the Temple of Aeyenlo"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

    return