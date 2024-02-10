label temple_of_aeyenlo_main:
    scene bg temple_of_aeyenlo with fade
    $ mc.location = Location.TEMPLE_OF_AEYENLO
    "Welcome to the Temple of Aeyenlo"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return