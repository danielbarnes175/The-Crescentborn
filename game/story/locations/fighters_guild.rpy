label fighters_guild_main:
    scene bg fighters_guild with fade
    $ mc_location = Location.FIGHTERS_GUILD
    "Welcome to the Fighter's Guild"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)
    
    return