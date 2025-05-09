# Splashscreen that loads on game startup
label splashscreen:
    scene black
    with Pause(1)

    show dabes_games_logo with dissolve
    with Pause(2)
    hide dabes_games_logo with dissolve

    return

# The game starts here.
label start:
    # We need some setup for the start of the game before we get to the normal time loop
    # Prologue
    $ mc_location = Location.UNKNOWN
    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT) 
    
    # Intro
    $ mc_location = Location.DREAM
    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)

    "Soon enough, class ends, and you have some free time to explore."
    if not free_time_tutorial_finished:
        call free_time_tutorial from _call_free_time_tutorial
    window hide
    show screen GameUI
    pause
    hide screen GameUI
    window show
    call day from _call_day_1
    call evening from _call_evening_1

    # Now we are in the normal time loop
    while True:
        # window hide
        show screen DayDisplay
        call change_day from _call_change_day
        call day_loop from _call_day_loop

    return

label credits:
    scene black
    show text "Credits" with dissolve
    with Pause(0.2)

    show text "The Crescentborn - dabes games" with dissolve
    with Pause(0.5)

    show text "Daniel Barnes, Michael Aiello, Dylan Szolomayer" with dissolve
    with Pause(0.5)

    show text """Music: Night of Mystery by Alexander Nakarada (www.creatorchords.com)
Licensed under Creative Commons BY Attribution 4.0 License
https://creativecommons.org/licenses/by/4.0/""" with dissolve
    show text """Music:  Vopna by Alexander Nakarada (www.serpentsoundstudios.com)
Licensed under Creative Commons BY Attribution 4.0 License
https://creativecommons.org/licenses/by/4.0/""" with dissolve
    show text """Music: Halloween Theme 1 by Alexander Nakarada 
Licensed under Creative Commons BY Attribution 4.0 License
https://creativecommons.org/licenses/by/4.0/""" with dissolve
with Pause(0.5)