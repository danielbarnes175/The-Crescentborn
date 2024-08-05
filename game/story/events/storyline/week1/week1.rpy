label scene_01_first_day:
    $ audio_crossFade(2, "audio/creepy_hallow.mp3")
    $ mc_location = Location.DREAM

    scene bg moon with fade

    "The moon shone down upon you. Trees rustled in the wind; a quiet night."
    "But it was not an altogether warm one; a chill ran down your spine."
    "But was it just the cold? The hair on the back of your neck stood on end."

    "Your eyes soon adjusted to the darkness. Your growing suspicions that you weren’t alone rang true, as with a start, you spotted a silhouette amidst the darkness. But you could make out little else; you couldn’t quite see who they were."
    show hreinar silhouette
    unknown_hreinar "The Crescentborn."
    unknown_hreinar "Given that this meeting is increasingly occuring, maybe we should introduce ourselves?"

    "As blurry as their form was, so too was their voice. It reverberated deep within you, but if you had to say whether the voice was male, female, loud, shrill, or at all defined… you could make no such statement."
    "It was if the shadow spoke without a voice at all, their words manifesting within your very mind."
    "The figure seemed to be waiting for your response."
    $ mc_name = renpy.input("What is your name?", default="MC", length=32)
    
    unknown_hreinar "We have joined once again, [mc_name]. I am ....... Have you yet realized thy purpose?"
    "When they said their name, you couldn't make out what they said. And before you had a chance to say anything more, the dream faded away."

    scene bg home_room with fade
    $ audio_crossFade(2, "audio/pickled_pink.mp3")
    $ mc_location = Location.DORM

    "Your eyes opened to blinding sunlight. It didn’t take long for them to adjust, and the details of your room soon came into focus."
    "A simple bed, an equally simple desk, and an open window take up the majority of the room."
    "The inn you'd chosen had been a simple one, after all--and cheap."

    "You sat up and swung your legs up and onto the floor. Cold sweat caked your forehead and clothes; it always did whenever you had this dream."
    "It was the same one you’d been having for a while now, but the more you had it the less you seemed to understand it."
    "{i}The Crescentborn.{/i}"
    "What did that mean? That was what the shadow always called you, but now just as ever it didn’t make any sense."

    "Similarly, the details of the dream began to fade just as they always had. You’d remember the shadow, that name, and little else."
    "Rubbing the last of the sleep out of your eyes, you decided you had better things to do than worry about some silly dream."

    "You grabbed the clothes you’d laid out the night before, dressing and heading down the stairs after grabbing your pack."
    "Today was your first day at the prestigious Balvor Tower, a magical academy at the heart of Eleria, your home country."
    "Well, perhaps not exactly the heart. Wizards liked their privacy after all, and it had been quite the hike from the royal capital to get here. But after many days of hard travel, you were finally at the end of your journey."

    scene bg path_to_school with fade
    "Seeing the Tower creep over the trees for the first time had been quite the sight, but the experience of setting foot within the walls simply couldn’t compare."
    "You had seen magic before, of course, but with so much magic gathered in one place, even the air itself felt different. Sweeter, more vibrant. It was hard to describe."

    "You walked amidst a crowd of humans, elves, and everything in between. Off in the distance, a pegasus and a wyvern looked like they were playing tag; if you squinted your eyes, you could just make out their riders."
    "*CRASH*"
    "Joy and wonder turned to pain and sorrow, as you found yourself suddenly sprawled out on the ground… and having dragged someone down with you."

    show kuviis annoyed
    kuviis "OW!"

    "You’d taken the worst of the fall and the girl in front of you was already back on her feet. And yelling."
    kuviis "Watch where you're going!"
    mc "What the?!"

    menu:
        "Apologize":
            show kuviis blush
            kuviis "Whatever, just pay attention next time!"
        "You watch where you're going!":
            kuviis "Oh, it's my fault? Yeah, ok. I'll get you a seeing-eye familiar, how's that sound. Ugh!"
    
    "The very rude girl stormed off, leaving you bewildered and a little annoyed."
    "Shaking your head, you stand back up as the small crowd of curious onlookers go back about their business. Your first day is off to quite the start."
    "You pushed the rude girl out of your mind as you refocused on finding your way. Helpful service gnomes guided you through the unfamiliar campus, leading you straight to something you could only describe as an advisor’s office. A wizened old woman sat behind the booth."
    
    scene bg advisors_booth with fade

    unknown_generic "Name, dear?"
    mc "[mc_name]"
    unknown_generic "I see. This'll be yours, then."
    "She spoke with a smile as she handed you a slip of paper."
    unknown_generic "Your schedule."

    "You took a look at the paper, excited to see what was in store for you. Instead, you frowned. There was only one class written down: Magical Studies."
    "You insisted there must be some mistake, but the old woman assured you it was correct."
    "First year students devoted their entire curriculum to this one class, she explained; it was only after completing the year-long project that you would disperse into the specialized classes of your choosing."
    "The spread of classes offered was enticing: alchemy, spell casting, magical engineering; the list went on. Clearly, you hadn’t been the first student to have asked that question, as the woman explained all of it without missing a beat."
    "Slightly disappointed, and just as bewildered, you stepped away from her booth and deeper into the complex."

    "Regardless of the situation with your classes, you were there to learn and make the most of the experience."
    "Balvor was famed for what it offered, so who knew what your future would hold?"

    "It was a shame you didn’t have very long to dwell on the possibilities. Balvor wasted no time in getting started, and your first class would be starting soon."
    "You knew you had just enough time to drop off your meager belongings in your assigned dormitory, so you headed there to quickly settle in."

    show bg room with fade
    "You appreciated the view your simple room offered, but the ringing of a dozen different bells pulled your attention back from the scenery."

    "It was time to head to class."

    return

label classroom_intro:
    scene bg classroom with fade
    $ mc_location = Location.CLASSROOM

    "You were surprised to find the room almost empty when you arrived. A handful of people had beaten you there, but most of the seats were still left unfilled."
    "You glanced at the large sheet of parchment nailed onto the wall, realizing it was a seating chart."
    "On the way to finding your seat, you realized that what you’d thought were desks were actually tables; a small handful of students could comfortably sit around them and have plenty of space for themselves. And with a start, you realized that your table was already occupied."

    show bluejay_hidden
    "You doubted you would have noticed the cloaked man with his hood drawn up, had you not sat at the same table. He nodded at you as you took your seat, but the gesture didn’t at all put you at ease. You couldn’t help but notice his eyes were hidden from view beneath that cowl."
    hide bluejay_hidden

    "Thankfully, you were saved from any awkward introductions by the arrival of, seemingly, the entire rest of the class all at once."
    "Streams of people poured in, each of them stranger than the last. It seemed as many elves as humans were in your class, along with a pair of orcs, a few humanoid beings you couldn’t quite place, and even a gnome."
    "Suddenly, the lone chair that stood a few feet taller than the rest made more sense."

    "As you watched the tide of students pour in, you had a strange thought. Had… had the room looked this big from the outside?"
    "There were already dozens of people inside, and dozens more on the way, whereas you had expected a classroom of maybe a dozen people at most."

    "One of the new arrivals headed your way, and you were right to think he was joining your group. A young man approached you and gave you a small smile."
    show ralph
    ralph "Pleasure to meet you,"
    "The man stuck out his hand."
    ralph "My name is Ralph Qurnaget. What's yours?"

    mc "[mc_name]."

    "Ralph smiled and turned to the stranger."
    ralph "And you?"
    hide ralph
    show bluejay_hidden
    "The hooded man nodded again, and said nothing."
    hide bluejay_hidden
    show ralph

    ralph "Interesting name..."
    "You were somewhat relieved when he took a seat between you and the mute stranger."
    "He was either an exceedingly healthy human or an elf, you couldn’t tell, but he seemed much more outgoing than the other stranger at your table."
    "A little blunt and to the point, but it was better than silence. He at least seemed like an honest person."

    "You decided to ask him a few questions while people were still filing in."
    $ _ralph_question_balvor = False
    $ _ralph_question_himself = False
    menu ralph_questions:
        "What would you like to ask Ralph?"
        "What do you know about Balvor?":
            $ _ralph_question_balvor = True
            ralph "You're new to the area, aren't you."
            mc "...I am..."
            ralph "Nothing wrong with being a traveler, but it explains quite a bit."
            mc "And you? Are you from around here?"
            ralph "Not exactly, but I’ve been in the area before. It’s an old town, I’ll tell you that. This place used to be a monastery from what I understand."
            ralph "Eventually it turned into a school, and grew to be quite famous. Originally only a handful of mages gathered here to study and research, and they became quite famous, making Balvor a famous name."
            ralph "The more famous Balvor became, the more mages flocked to its halls. The more mages made a name for themselves here, the more famous the Tower became. Make sense?"
            menu:
                "I guess so...":
                    pass
                "No, not really...":
                    pass
            ralph "Well, as the school grew, it needed to get bigger to fit more students, staff, experiments, and so on."
            ralph "The Tower is still the centerpiece, but a dozen different buildings sprang up around it, even other towers. It’s a small castle now more than anything else, really."
            ralph "And try as they might, the mages couldn’t stop new towns springing up right next door. Praelor’s the only one that’s worth mentioning; the others are simple hamlets, really. Not much to mention about them."
            jump ralph_questions

        "Tell me about yourself.":
            $ _ralph_question_himself = True
            ralph "Truth be told, I’d rather not. I prefer to keep to myself for the most part, but I’m looking forward to learning to harness magic."
            ralph "If you ever want a partner to practice with, I would be interested in testing myself against you."
            mc "...O...kay..."
            jump ralph_questions

        "Don't ask anymore questions." if _ralph_question_balvor and _ralph_question_himself:
            pass

    "Out of the corner of your eye, you noticed that one of the orcs was seemingly going in circles. You thought you’d seen her before, and you soon realized why: she was lost."
    "She’d already passed by your table twice, and was clearly growing more and more anxious the longer it took for her to find her seat."