init python:
    from enum import Enum

    class Time(Enum):
        ANY = "Any"
        MORNING = "Morning"
        MIDDAY = "Midday"
        EVENING = "Evening"
        NIGHT = "Night"

    class DayOfWeek(Enum):
        MONDAY = "Monday"
        TUESDAY = "Tuesday"
        WEDNESDAY = "Wednesday"
        THURSDAY = "Thursday"
        FRIDAY = "Friday"
        SATURDAY = "Saturday"
        SUNDAY = "Sunday"

    def advance_time():
        if time_of_day == Time.MORNING:
            renpy.jump("day")
        elif time_of_day == Time.MIDDAY:
            renpy.jump("evening")
        elif time_of_day == Time.EVENING:
            renpy.jump("morning")  # Assuming the loop starts again in the morning
        else:
            renpy.error("Invalid time of day")

label day_loop:
    call morning from _call_morning
    call day from _call_day
    call evening from _call_evening

    return

label change_day:
    $ total_day_number += 1
    $ day_number += 1

    if day_number == 8:
        $ day_number = 1
        $ week_number += 1

    if day_number == 1:
        $ day_of_week = DayOfWeek.MONDAY
    elif day_number == 2:
        $ day_of_week = DayOfWeek.TUESDAY
    elif day_number == 3:
        $ day_of_week = DayOfWeek.WEDNESDAY
    elif day_number == 4:
        $ day_of_week = DayOfWeek.THURSDAY
    elif day_number == 5:
        $ day_of_week = DayOfWeek.FRIDAY
    elif day_number == 6:
        $ day_of_week = DayOfWeek.SATURDAY
    elif day_number == 7:
        $ day_of_week = DayOfWeek.SUNDAY

    return

label morning:
    scene bg room with fade
    $ time_of_day = Time.MORNING
    $ mc_location = Location.DORM
    "You got up and started to get ready for the day. After getting ready, you made your way to class."

    $ mc_location = Location.CLASSROOM

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

    "Time passed by..."
    return

label day:
    scene bg classroom with fade
    $ time_of_day = Time.MIDDAY
    $ mc_location = Location.CLASSROOM
    if not free_time_tutorial_finished:
        call free_time_tutorial

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

    "It is the middle of the day. You have some free time."
    window hide
    show screen GameUI
    pause
    hide screen GameUI
    window show

    "Time passed by..."
    return

label evening:
    scene bg moon with fade
    $ time_of_day = Time.EVENING
    $ mc_location = Location.DORM

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)

    "It is the end of the day. You have some free time."
    window hide
    show screen GameUI
    pause
    hide screen GameUI
    window show
    
    "Time passed by..."
    return
