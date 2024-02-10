label balvor_tower_main:
    scene bg balvor_tower with fade
    $ mc.location = Location.BALVORS_TOWER
    "Welcome to Balvor Tower"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return