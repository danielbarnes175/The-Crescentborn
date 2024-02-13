label balvor_tower_main:
    scene bg balvor_tower with fade
    $ mc_location = Location.BALVORS_TOWER
    "You made your way over to Balvor Tower"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)
    
    return