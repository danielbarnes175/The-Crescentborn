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
    $ day_number = 1
    $ week_number = 1
    $ time_of_day = Time.MORNING
    $ mc_location = Location.UNKNOWN

    call scene_00_prologue
    call scene_01_first_day

    # play music "audio/creepy_hallow.mp3"
    # $ mc_location = Location.DREAM

    # scene bg moon with fade

    # "The moon shone down on you. You felt a chill run up your spine."
    # "Your eyes adjusted to the darkness."
    # "There was someone there. You couldn't quite make out who they were."
    # show hreinar silhouette
    # unknown "Ah, it's you again. The Crescentborn. Given that this meeting is increasingly occuring, maybe we should introduce ourselves?"
    # $ mc_name = renpy.input("What is your name?", default="MC", length=32)
    # unknown "[mc_name], huh? It's a pleasure to make your acquantaince. Ah it looks like you're already beginning to wake up..."
    # unknown "My introduction will have to come another time then. I hope that we see each other {i}a lot{/i} more..."

    # scene bg room with fade

    # "Your eyes slowly opened. It was that dream again."
    # "You've been having the same dream for a while now. It would always show a person in front of the moon. They would always be speaking to you."
    # "You never could remember what they were saying though. This time was actually the first time you could."
    # "'The Crescentborn' - what does that mean? It doesn't make sense."
    # "You stood up out of bed. You didn't have all day to ponder over it. You had to get ready for class."

    # scene bg room with fade
    # play music "audio/pickled_pink.mp3"
    # $ mc_location = Location.DORM

    # "Today was your first day at the Balvor Tower, a magical academy in the middle of Eleria, the country you've lived your entire life in."
    # "You took a look at your schedule, and slightly frowned. It only had one class on it, 'magical studies'."
    # "You had checked it with your advisor a few times, but she ensured you that it was correct. First years take a single class where they do a project with other students of all majors."
    # "Then, after your first year, then you would take specialized classes. When you enrolled in this school, you expected to learn a variety of subjects."
    # "Alchemy, spell casting, magical engineering, you name it. Typical academies had all of those subjects."
    # "For some reason, though, the Balvor Tower only had the one magical studies class, and by the time you realized, it was too late to find another university."
    # "Regardless, you were here to learn and make the most of your experiences. It was your first year in university, and you were excited. Who knows what the future would hold?"
    # "Well, you didn't have all day to wonder about it. It was time to head to class."
    
    call classroom_intro from _call_classroom_intro

    while True:
        # window hide
        show screen DayDisplay
        call change_day from _call_change_day
        call day_loop from _call_day_loop

    return