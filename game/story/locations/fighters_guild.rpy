label fighters_guild_main:
    scene bg fighters_guild with fade
    $ mc.location = Location.FIGHTERS_GUILD
    "Welcome to the Fighter's Guild"

    $ trigger_events(main_story_events)
    $ trigger_events(character_events)
    
    return