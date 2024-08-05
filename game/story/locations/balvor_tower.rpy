label balvor_tower_main:
    scene bg balvor_tower with fade
    $ mc_location = Location.BALVOR_TOWER
    "You made your way over to Balvor Tower"

    $ trigger_events(main_story_events, Event_Type.MAIN_STORY_EVENT)
    $ trigger_events(character_events, Event_Type.CHARACTER_EVENT)
    
    return

label balvor_tower_exploration:
    $ mc_location = Location.BALVOR_TOWER
    scene bg balvor_tower_outside with fade
    "You decided to explore more of the Tower itself. All of your classes had taken place inside this tower, and yet, you hadn't actually fully explored the building. Class had been interesting, and you’d met many intriguing people, but the mysteries behind the Tower were just as compelling as anything within it."
    "Everyone called it Balvor Tower due to the massive stone spire in the center, but it was actually a collection of about 9 or 10 smaller towers surrounding the center one. There was a library, various laboratories, shops, stalls, a stable here and there for some of the more grounded familiars."
    "Of course, it was the namesake structure which drew your attention the most, and where better to start exploring your new home than the Tower itself?"

    "Hardly any door seemed locked, and you hadn’t seen anything resembling a guard or security since you’d arrived. Curiosity got the better of you, and so you took the first staircase you could find."
    scene bg balvor_tower_staircase with fade
    "Muffled conversations from beneath large oak doors told you that, despite the first years being dismissed for the day, many classes were still in session. Occasionally you would find a room with a window, and you’d sneak glances at more advanced magic at play."
    "Even for more advanced students, it was still just the first day, so the most you saw was theory and introductory lessons. Still, the bits and pieces you picked up got you excited for the future of your education."

    "But the roadblock of picking a relic stopped the excitement in its tracks. Without a relic, you’d hardly be able to perform much magic at all, and you still had no idea where to even start."
    "You climbed another set of stairs, and realized the Tower was quieter now. In fact, it grew more and more quiet with each passing level, and you wondered if most of its occupants were still outside. Most of their resources must be on welcoming the new academic year, you reasoned."

    scene bg balvor_tower with fade
    $ audio_crossFade(2, audio_main_hreinar)
    "But it wasn’t long before you felt the hairs on the back of your neck stand on end. You turned around, heart racing. Were you… were you truly alone?"
    "As long as you stared, nobody ever revealed themselves. The empty stone hallway was just that… empty."
    "You shook off most of your nerves. It was still an unfamiliar place, after all. You kept exploring."
    "But the feeling never left. It was almost as if the longer you explored, the worse it got. You started checking every corner. Every noise perked your ears. The feeling of foreboding only grew worse and worse."
    "It got to the point where, when you thought you reached the last staircase, you’d broken out in a cold sweat. You turned around again, but the dark hallway didn’t alleviate your newfound fear. You checked your pulse; your heart was beating far harder than a casual walk should have elicited."
    "{i}Maybe… maybe I should go back. Maybe I’m not allowed up here after all...{/i}"
    "For some reason, you felt like you shouldn’t make a sound."
    "You turn around, having lost your nerve. It was just a tower; you could get a good view from elsewhere."
    scene bg balvor_tower_staircase with fade
    "You hurried back down, taking the stairs without hesitation. On the way up, you’d been curious to check every detail, but on the way down, you were just eager to leave."
    "{i}Why? What is this feeling?{/i}"
    "It wasn’t until you were another few stories down that you realized the feeling was fading. If you strained your ears, you could hear voices and conversation: classes. You weren’t alone anymore, and that was making it easier to forget the fear you’d felt just a few minutes ago."
    "You were suddenly glad you had been alone; it seemed childish to be so afraid of an empty tower. Still, you decided not to try to reach the top a second time. Maybe another day."
    scene bg balvor_tower_outside with fade
    "You find your way back to ground level, realizing that a fair bit of time had passed. You’d been in the Tower for several hours."
    $ audio_crossFade(2, "audio/pickled_pink.mp3")

    return