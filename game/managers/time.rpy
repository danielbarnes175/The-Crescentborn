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
        $ day_of_week = "Monday"
    elif day_number == 2:
        $ day_of_week = "Tuesday"
    elif day_number == 3:
        $ day_of_week = "Wednesday"
    elif day_number == 4:
        $ day_of_week = "Thursday"
    elif day_number == 5:
        $ day_of_week = "Friday"
    elif day_number == 6:
        $ day_of_week = "Saturday"
    elif day_number == 7:
        $ day_of_week = "Sunday"

    return

label morning:
    scene bg room
    with fade
    $ time_of_day = "Morning"
    "You got up and started to get ready for the day."
    
    return

label day:
    scene bg classroom
    with fade
    $ time_of_day = "Midday"
    "It is the middle of the day."

    return

label evening:
    scene bg moon
    with fade
    $ time_of_day = "Evening"
    "It is the end of the day."
    
    return
