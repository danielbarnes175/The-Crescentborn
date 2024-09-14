label scene_01_first_day:
    $ scene_01_first_day.triggered = True
    $ (main_story_events.get("scene_01_first_day")).scene_triggered = True
    $ audio_crossFade(2, audio_main_hreinar)
    $ mc_location = Location.DREAM

    scene bg moon with fade

    "The moon shone down upon you. Trees rustled in the wind; a quiet night."
    "But it was not an altogether warm one; a chill ran down your spine."
    "But was it just the cold? The hair on the back of your neck stood on end."

    "Your eyes soon adjusted to the darkness. Your growing suspicions that you weren’t alone rang true, as with a start, you spotted a silhouette amidst the darkness. But you could make out little else; you couldn’t quite see who they were."
    show hreinar silhouette
    unknown_hreinar "The Crescentborn."
    unknown_hreinar "Given that this meeting is increasingly occuring, maybe we should introduce ourselves?"

    "As blurry as their form was, so too was their voice. It reverberated deep within you, but if you had to say whether the voice was male, female, loud, shrill, or at all defined... you could make no such statement."
    "It was if the shadow spoke without a voice at all, their words manifesting within your very mind."
    "The figure seemed to be waiting for your response."
    $ mc_name = renpy.input("What is your name?", default="MC", length=32)
    
    unknown_hreinar "We have joined once again, [mc_name]. I am ....... Have you yet realized thy purpose?"
    "When they said their name, you couldn't make out what they said. And before you had a chance to say anything more, the dream faded away."

    # scene bg home_room with fade
    scene bg room with fade
    $ audio_crossFade(2, audio_main_free_time)
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
    scene bg path_to_school with fade
    "Today was your first day at the prestigious Balvor Tower, a magical academy at the heart of Eleria, your home country."
    "Well, perhaps not exactly the heart. Wizards liked their privacy after all, and it had been quite the hike from the royal capital to get here. But after many days of hard travel, you were finally at the end of your journey."

    scene bg inside_the_walls with fade
    "Seeing the Tower creep over the trees for the first time had been quite the sight, but the experience of setting foot within the walls simply couldn’t compare."
    "You had seen magic before, of course, but with so much magic gathered in one place, even the air itself felt different. Sweeter, more vibrant. It was hard to describe."

    "You walked amidst a crowd of humans, elves, and everything in between. Off in the distance, a pegasus and a wyvern looked like they were playing tag; if you squinted your eyes, you could just make out their riders."
    $ audio_crossFade(1, audio_main_kuviis)
    "*CRASH*"
    "Joy and wonder turned to pain and sorrow, as you found yourself suddenly sprawled out on the ground... and having dragged someone down with you."

    show kuviis annoyed
    unknown_kuviis "OW!"

    "You’d taken the worst of the fall and the girl in front of you was already back on her feet. And yelling."
    unknown_kuviis "Watch where you're going!"
    mc "What the?!"

    menu:
        "Apologize":
            show kuviis blush
            unknown_kuviis "Whatever, just pay attention next time!"
        "You watch where you're going!":
            unknown_kuviis "Oh, it's my fault? Yeah, ok. I'll get you a seeing-eye familiar, how's that sound? Ugh!"
    
    "The very rude girl stormed off, leaving you bewildered and a little annoyed."
    "Shaking your head, you stand back up as the small crowd of curious onlookers go back about their business. Your first day was off to quite the start."
    "You pushed the rude girl out of your mind as you refocused on finding your way. Helpful service gnomes guided you through the unfamiliar campus, leading you straight to something you could only describe as an advisor’s office. A wizened old woman sat behind the booth."
    $ audio_crossFade(2, audio_main_free_time)
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

    call classroom_intro from _call_classroom_intro

    return

label classroom_intro:
    scene bg classroom with fade
    $ mc_location = Location.CLASSROOM

    "You were surprised to find the room almost empty when you arrived. A handful of people had beaten you there, but most of the seats were still left unfilled."
    "You glanced at the large sheet of parchment nailed onto the wall, realizing it was a seating chart."
    "On the way to finding your seat, you realized that what you’d thought were desks were actually tables; a small handful of students could comfortably sit around them and have plenty of space for themselves. And with a start, you realized that your table was already occupied."

    show bluejay hidden
    "You doubted you would have noticed the cloaked man with his hood drawn up, had you not sat at the same table. He nodded at you as you took your seat, but the gesture didn’t at all put you at ease. You couldn’t help but notice his eyes were hidden from view beneath that cowl."
    hide bluejay hidden

    "Thankfully, you were saved from any awkward introductions by the arrival of, seemingly, the entire rest of the class all at once."
    "Streams of people poured in, each of them stranger than the last. It seemed as many elves as humans were in your class, along with a pair of orcs, a few humanoid beings you couldn’t quite place, and even a gnome."
    "Suddenly, the lone chair that stood a few feet taller than the rest made more sense."

    "As you watched the tide of students pour in, you had a strange thought. Had... had the room looked this big from the outside?"
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
    show bluejay hidden
    "The hooded man nodded again, and said nothing."
    hide bluejay hidden
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
    "Curiosity got the better of you, and you leaned over to ask Ralph another question."
    mc "Do you know who she is?"
    ralph "The orc?"
    mc "Yeah. The one that looks lost."
    ralph "I don’t know her. But her kind is rather rare this far north."
    ralph "In my experience, orc shamans don’t care very much for formal magic, relying on rituals and traditional alchemy instead. She’s either very intelligent, or grew up away from mainline orc society."
    mc "Do you have something against orcs?"
    ralph "Not necessarily. Aside from lifespan, there isn’t much separating an elf from a man, or a man from an orc. True, elves tend to be more gifted in magic than the other races, but they have centuries to hone their skills."
    ralph "If a man or an orc could live a millenia, they would be no different."
    mc "Don’t you have to be invited to Balvor?"
    ralph "You do. Which means whoever she is, Balvor’s mages think she is worthy of this education. I certainly won’t be underestimating her, and neither should you."
    hide ralph

    show gudrak embarrassed
    "You began to notice that other students had realized the orc’s predicament as well. You never liked to see someone be the center of unwanted attention, so you stood up from your desk and walked towards her."
    mc "What’s your name?"
    "Her eyes darted every which way, but never landed on your own."
    gudrak "G-gudrak."
    mc "Gudrak?"
    "She nodded, and then you heard a voice coming from the side."

    show gudrak embarrassed:
        linear 0.3 xalign 0.3
    show ralph with moveinright:
        xalign 0.7 yalign 1.0

    ralph "She sits over here."
    mc "W-How do you...?"
    ralph "I saw her name next to mine."
    mc "And you remembered?"
    ralph "Of course."
    "You frowned and remembered the earlier conversation where Ralph asked for your name."
    mc "Then, did you know..?"
    ralph "Yours? Of course."
    "You pointed at the hooded man still seated."
    mc "Then what's--"
    "Ralph gave a dismissive wave of his hand."
    ralph "I'll leave that up to him. If he doesn’t want to indulge, then I won’t either."
    ralph "Names are powerful things. It can be safer sometimes to keep yours a secret."

    hide ralph
    "You tear your eyes away from Ralph, and back to Gudrak. She was still rooted in place."
    mc "Well, c’mon then. Looks like you’re with us."
    "You beckon for her to follow, and you’re relieved to see her doing just that. As you take your seat next to Ralph, Gudrak takes her seat next to you."
    hide gudrak embarrassed
    mc "Isn't everyone here yet?"

    show ralph
    ralph "There {i}is{/i} a fifth, you know"
    "You eyed the last vacant seat."
    mc "A fifth? Who's--?"
    unknown_kuviis "Seriously?!"
    hide ralph
    "You turn and find none other than the girl who’d so rudely run into you earlier that day."
    show kuviis annoyed
    mc "You're a first-year?!"
    unknown_kuviis "Would you prefer to have tackled a senior?"

    show kuviis annoyed:
        linear 0.3 xalign 0.3
    show ralph with moveinright:
        xalign 0.7 yalign 1.0

    ralph "I’m glad you two already know each other."
    unknown_kuviis "As if."
    "She noticeably brightened when she turned away from you, and instead to Ralph."
    show kuviis:
        linear 0.3 xalign 0.3

    kuviis "My name is Kuviis. Kuviis Bailey. My mother’s an elf from Wyrmcreek. I expect this to be an exciting semester."
    ralph "Well, Kuviis, my name is Ralph Qurnaget. This one is Gudrak--sorry, I never caught your surname."

    show kuviis:
        linear 0.3 xalign 0.15
    show ralph at center with moveinright
    show gudrak with moveinright:
        xalign 0.9 yalign 1.0

    gudrak "Gro-Tigor."
    ralph "Gudrak gro-Tigor, and you already know [mc_name] of course."
    "Kuviis rolled her eyes. She turned to the last member of their group, extending her hand."
    kuviis "And you are?"
    "The stranger leaned forward, folding his hands on the table before speaking in a surprisingly gruff and grizzled voice."
    
    show kuviis:
        linear 0.3 xalign 0
    show ralph:
        linear 0.3 xalign 0.3
    show gudrak:
        linear 0.3 xalign 0.65
    show bluejay hidden with moveinright:
        linear 0.3 xalign 0.99


    bluejay "Eignar."
    "You’d almost thought he wouldn’t ever speak, but it was a relief to find out that he could."
    kuviis "Eignar. Pleased to meet you."
    "The female elf took her seat next to Eignar."

    hide kuviis
    hide ralph
    hide gudrak
    hide bluejay hidden

    "It was only another few minutes before someone entered the room that you knew immediately to be more than just a student. Having observed the classroom for some time, you knew you and your fellow students came in all shapes, sizes, ages, and races, but the older woman who walked to the center of the classroom was clearly no novice."
    "The regal robes with intricate markings all along their length weren't befitting some random traveler. When she spoke, you knew at once that this was one of the hallowed mages of Balvor Tower."

    show headmistress_sullon
    headmistress_sullon "Good morning."
    "Her voice rang out throughout the classroom, clear as day. {i}'Magic?'{/i} you think to yourself."

    headmistress_sullon "I see you’ve all found your seats. Good; some of them can be quite good at hiding."
    "She had half a smile, but continued without expecting any response."
    headmistress_sullon "Consider yourselves having passed the first test."
    "She clasped her hands behind her back and began pacing back and forth."
    headmistress_sullon "Now, how about an introduction? This is Balvor Tower, of course, and you will be the class of 755. And my name is Headmistress Shayarun Sullon. I am the Archmage of Balvor, and your teacher for this first year."

    "You heard quite a few people whispering and murmuring to one another, but the Headmistress only smiled until they fell silent. She then continued her introduction."
    headmistress_sullon "Over the course of the year, you’ll learn a great deal about magic; more than you’d ever expected I’m sure. But as much as I’m sure there are some experts here already, I know we also have some novices who have never so much as cast a spell before in their life."
    headmistress_sullon "So, what is magic? It’s the result of much study, care, and precision -- but at its simplest, it’s the harnessing of the life energy we all have within us. Some are graced with more than others, but we all have it."
    headmistress_sullon "It’s part of what makes life possible. And to use magic is to recognize that there is magic within you. You must feel it, and then will it into the shape and forwsm you want."
    headmistress_sullon "One can cast a spell with mere words, or even thought, but there is a much more straightforward way to do it: to use a medium. A conduit. A relic, if you will. Observe."

    "She undid her necklace and held it up for the class to see."
    headmistress_sullon "My relic is this necklace I inherited from my mother, who inherited it from her mother, who inherited it from her mother, who claimed to have found it in a cornfield, but I digress."

    "She put it on the table and held out a hand."
    headmistress_sullon "Here is one of the simplest spells you can learn. Fire!"
    "She waved her hand towards an unlit series of candles. Flames spewed out from her palm, lighting each one. The class clapped politely."
    "She started to speak again, slipping the necklace back on."
    headmistress_sullon "And now when one possesses a relic, Magic becomes much more potent. Fire!"
    "She did the same motion as last time, but this time towards a suit of armor in the corner. Blue flame, not red, lit the room this time, forcing half the class nearest her to duck down behind their desk for the heat."
    "It was so bright, you had to close your eyes, and when you opened them again, the suit of armor was a molten heap of still white-hot slag."
    "The Headmistress was positively giggling."
    headmistress_sullon "I’m sorry. Sometimes I get a little too fired-up with the demonstrations. Oh and don’t worry about the armor, I’ll fix that right up after introductions."
    headmistress_sullon "Relics not only act as a guide towards your own magical energy, but they amplify it as well. The inner workings of relics are too complicated for an introduction, but think of them as a key that will unlock your potential."
    headmistress_sullon "Without relics, magic is possible, but it is generally weaker and more difficult. If a relic is the key to a locked door, then going without a relic is like picking the lock; as in, your own concentration."
    headmistress_sullon "With time, you learn the lock and can open it quicker each time, but with a relic, you can put all of your energy into the power behind the spell, not the method. It may not make sense now, but it will soon, I assure you."

    "The Headmistress paused for a moment to see if anyone had any questions before moving on."
    headmistress_sullon "This leads me nicely into the topic of this class: relics! You’ll all need one if you want to start casting spells sometime this year, so the focus of the next two semesters will be creating your very own relics."
    headmistress_sullon "It must be something tailored to you, so you can’t just pick any old thing. The more attuned you are to the relic of your choice, the better it will work for you. Family heirlooms, for example, work well for this purpose, though there are plenty of other options."
    headmistress_sullon "This project will be much faster if you have someone to bounce ideas off of--so I’ve placed all of you into groups. I’ve tried to match people of various personalities and backgrounds to facilitate as many opportunities for the cross-pollination of ideas as possible, so talk! Introduce yourselves!"
    headmistress_sullon "This first lesson will be mainly introductory, so don’t worry about the relic too hard for the next few hours! Just start brainstorming!"

    "She clapped her hands a few times and waved everyone to start talking amongst themselves. A few people, you noticed, watched her as she turned and started waving at the remains of the suit of armor, which started to reform before your very eyes."
    hide headmistress_sullon
    show kuviis with moveinbottom

    kuviis "Well, {i}I{/i} already have a relic in mind."
    mc "What? It’s only been like two minutes since we even learned about them."
    kuviis "I’ve been learning magic since I could talk. I knew a thing or two about relics before joining Balvor, you know. Didn’t you do any research beforehand?"

    "You were saved the embarrassment of admitting that, no, you hadn’t, by Eignar - of all people - coming to your rescue."
    
    show kuviis:
        linear 0.3 xalign 0.3
    show bluejay hidden with moveinright:
        xalign 0.7 yalign 1.0

    bluejay "People come from different backgrounds, Kuviis. Some of us don’t see a lot of magic before coming to places like this."
    "You looked at Kuviis to see her reaction, only to see her face brimming with genuine curiosity."
    kuviis "So where are you from?"
    bluejay "East."
    "He pulled his hood back, revealing a scarred face that, when he was younger, would have been quite handsome."
    
    show bluejay with moveinright:
        xalign 0.7 yalign 1.0

    bluejay "I’ve spent the last thirty years as a mercenary. Let’s just say I’ve had enough of that life."
    kuviis "A mercenary? Would I know which band?"
    bluejay "Unfortunately. The Blue Arrows."
    kuviis "Ah! I have heard of that one. How exciting. You wouldn’t happen to be one of the famous ones, would you?"
    bluejay "Hardly. I doubt you’ve heard the name ‘Bluejay’ before, have you?"
    kuviis "Hmm..."
    kuviis "No, I don't think so."
    bluejay "Then I did my job well."
    mc "Bluejay?"
    
    show kuviis:
        linear 0.3 xalign 0.15
    show bluejay at center with moveinright
    show ralph with moveinright:
        xalign 0.9 yalign 1.0

    ralph "I wasn’t lying when I said that was an interesting name."
    bluejay "Call me that, if you’d like. There’s nobody alive who would recognize me by that name. At least, if there was, I wouldn’t be here telling you about it."
    kuviis "And now you’re studying magic?"
    bluejay "It’s something different. Something... more certain."
    kuviis "Hmmm... I see. Well, best of luck figuring out your relic."
    mc "Speaking of which..."
    hide kuviis
    hide bluejay
    hide ralph
    "You rack your brain trying to think of a relic, but nothing comes to mind. You wish you had a family heirloom like the Headmistress did, but alas, you’re just a lowly orphan. You decide to ask your group what their thoughts on their relics are."
    menu ask_project_questions:
        "Who would you like to ask?"
        "Ralph":
            menu ask_project_questions_ralph:
                "What would you like to ask Ralph?"
                "Do you have any ideas, Ralph?":
                    show ralph
                    ralph "A few. Some are better than others."
                    mc "Like what?"
                    ralph "Maybe a hilt, or a jewel embedded in a scabbard. Something small that can be added on to something I’m already carrying."
                    mc "I see..."
                    hide ralph
                    jump ask_project_questions_ralph
                "Do you know how to use magic?":
                    show ralph
                    ralph "I do. I’ve had plenty of practice, of course, so I don’t think it should come as a surprise."
                    mc "How much practice have you had?"
                    ralph "Only about three-hundred years, but I’m a fast learner."
                    mc "T-three hundred?!"
                    show ralph:
                        linear 0.3 xalign 0.3
                    show kuviis with moveinright:
                        xalign 0.7 yalign 1.0
                    kuviis "Well yeah, he's an elf. Didn't you notice?"
                    mc "You said you're an elf too, so how old are you then?"
                    kuviis "You're really asking a woman her age?"
                    "You decided not to press your luck..."
                    hide kuviis
                    hide ralph
                    jump ask_project_questions_ralph
                "Ask someone else.":
                    jump ask_project_questions
        "Eignar":
            menu ask_project_questions_eignar:
                "What would you like to ask Eignar?"
                "Eignar, do you know what you’re doing yet?":
                    show bluejay
                    bluejay "No. But I don’t need anything fancy. Something small and unassuming will do. I’d rather not stick out if I can help it."
                    hide bluejay
                    jump ask_project_questions_eignar
                "What was being a mercenary like?":
                    show bluejay
                    bluejay "I thought it would be an adventure. For a time, it was, but being a mercenary is like being a soldier, just without the job security. Onwards and upwards, however. Even the acorn eventually changes."
                    hide bluejay
                    jump ask_project_questions_eignar
                "Ask someone else.":
                    jump ask_project_questions
        "Kuviis":
            menu ask_project_questions_kuviis:
                "What would you like to ask Kuviis?"
                "You sound like you know a lot about magic. Are you a noble or something? How’d you learn so much?":
                    show kuviis
                    kuviis "I’m a half-elf. Elves are very powerful mages, and even if they don’t practice for thousands of years they still get the wisdom of someone who has. Let’s just say I had really good teachers."
                    hide kuviis
                    jump ask_project_questions_kuviis
                "What’s your relic going to be?":
                    show kuviis
                    kuviis "Well it wouldn’t be any fun if I just told you now, would it? What if you steal my idea?"
                    mc "Why would I steal your idea? Can’t two people have the same kind of relic?"
                    "For once, Kuviis looked at you with sincerity."
                    show kuviis blush
                    kuviis "I’m ok helping inspire someone, but after a certain point inspiration turns into influence. Picking your relic should be your own choice. Maybe ask me again once you’ve got some concrete ideas."
                    hide kuviis
                    jump ask_project_questions_kuviis
                "Ask someone else.":
                    jump ask_project_questions
        "Gudrak":
            menu ask_project_questions_gudrak:
                "What would you like to ask Gudrak?"
                "I haven’t seen many orcs around here. How’d you end up at Balvor?":
                    show gudrak
                    gudrak "I... I found some old tomes back home. They’re really valuable, and well, Balvor asked if they could keep them here for safekeeping."
                    gudrak "Of course I said yes, but then they asked if I’d like to be a student too! I... I just couldn’t pass up that chance..."
                    mc "You like books?"
                    gudrak "Yes! When I graduate, I’d like to do something with them. Work in an arcanum, or do some sort of research. Maybe even something with architecture?"
                    mc "...Amazing. I don't have any idea what I want to do when I graduate."
                    hide gudrak
                    jump ask_project_questions_gudrak
                "Do you have any ideas for your relic?":
                    show gudrak
                    gudrak "Not... not really. A few ideas, maybe... Is it weird to make your relic a book? But... what book would I pick? Where would I keep it? It’d be weird to carry a book around all day, wouldn’t it? I don’t know..."
                    "You didn’t think you’d get very many ideas from Gudrak this early on."
                    hide gudrak
                    jump ask_project_questions_gudrak
                "Ask someone else.":
                    jump ask_project_questions
        "Don't ask anything more.":
            pass

    "Despite the conversation, you felt no closer to figuring out a relic than when you began."
    "You discussed the relic project for some time longer before the Headmistress called for your attention again."
    show headmistress_sullon
    headmistress_sullon "Now, there will be plenty of time for discussion and brainstorming throughout the next few weeks. But in the meantime, it’s time to get started on the theory..."
    "You pulled out a piece of parchment, ready to take notes, but found yourself distracted the whole way through. This relic business was already shaping up to be more difficult than you’d expected, and it was only the first day."

    hide headmistress_sullon
    return

label second_dream:
    $ second_dream.triggered = True
    $ audio_crossFade(2, audio_main_hreinar)
    $ mc_location = Location.DREAM

    scene bg moon with fade
    "It was the same black forest. Clouds shifted, allowing moonlight to pour over the clearing for but a moment, before the skies obscured it again."
    show hreinar silhouette
    "The mottled gray and white made it difficult to focus on the figure before you, but you knew you wouldn’t be able to anyway. It was the same shadow you always saw, and just like the others, this time they were just as hazy, like their outline wasn’t solid."

    unknown_hreinar "Crescentborn."
    "Always the same name. Always the same mystery."
    unknown_hreinar "Your heart is still weak, your soul fragile... grow stronger, my child. You have many allies beside you, but time... time is not one of them..."
    hide hreinar silhouette with Dissolve(1)
    "You blinked; the shadow was gone. It was like it had dissolved before your very eyes."
    "The clouds shifted again, and moonlight streamed down again. You looked up to meet it, the light almost blinding from amidst the darkness. You raised your arms to cover your eyes. The last thing you saw before waking, in another cold sweat, was a full moon."
    $ audio_crossFade(2, audio_main_free_time)

    return