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

    scene bg room with fade
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
    "You walk into the classroom. There's a list of seating arrangements, which you thought was a little strange, but you found your name and moved over to your table."
    "The rest of the class soon filtered in. There seemed to be people of all shapes and sizes."
    "Your table mates came in as well, but you did your best not to stare, so you pretended to daydream and stare off into space."
    "Eventually the professor walked in, and introduced himself."

    show professor
    professor "Good morning class. I'll be your professor for the year. If you haven't heard already, the Balvor Tower curriculum is different than most academies in Eleria."
    professor "Rather than place you into classes specific to your chosen area of study, we have the first years work on a single magical project for the year."
    professor "The details of this project will be discussed in time, but for now, take a look at your classmates sitting next to you. These people will be your group members for the year. So go on and introduce yourselves."
    hide professor

    "I looked around at my group, and my eyes got stuck on one member in particular."
    show gudrak embarrassed
    "I realized I was staring at a half-orc girl who had about a foot and a half on me. I looked around, and everybody else was staring at her too."
    "She looked like she was about to pass out, so I decided to help her."
    mc "Hey everyone. My name is [mc_name]. I'm [mc_age] and I'm here to study defensive magic."
    "Seeing a few blank stares, I decided to give a little more detail."
    mc "You know, like spells you would use to protect a house from rain, or to fight off bandits."
    "I looked at the half-orc girl again. She seemed relieved all the attention was off her, so I was surprised when she spoke up next."
    show gudrak
    gudrak "O-okay, um, hi. My name is Gudrak, I'm 28-I mean 29 years old, and I, uh, work in the library."
    "She started to shrink back in her chair."
    show gudrak embarrassed
    with dissolve
    gudrak "I'm studying tome making with a minor in tower construction."
    "Tower construction...?"
    "Another girl spoke up."
    show gudrak embarrassed:
        linear 0.3 xalign 0.3
    show kuviis with moveinright:
        xalign 0.7 yalign 1.0
    kuviis "Tower construction? Like how?"
    hide gudrak embarrassed
    show gudrak:
        xalign 0.3 yalign 1.0
    gudrak "Oh, like for wizard towers. I-i thought that, since I'm a half-orc, and I wanna be a mage, that there's probably not that many mages who can do physical labor. This way I can do both!"
    "She seemed a lot more confident than she was a second ago."
    "The conversation turned to the next introduction but not before I saw Gudrak mouth the words \"thank you\" out of the corner of my eye."
    kuviis "Alright then. I guess I'm up next."

    
    hide gudrak
    with dissolve
    "We all turned to look at the young half-elf."
    hide kuviis
    show kuviis at center
    with move
    kuviis "My name is Kuviis Bailey. I'm here because my home life was getting quite boring, and I figured that this Academy would add a little excitement."
    kuviis "It'll at least be interesting, judging by the curriculum. Oh, I should also mention that I'm majoring in poetry."
    "This time it was you asking a question."
    mc "You've come to a magical academy to study poetry?"
    show kuviis annoyed
    kuviis "Yes, is there something wrong with that?"
    "You could tell by the tone in her voice that she this probably wasn't a battle you should fight."
    mc "N-no, of course not... Why don't we move on? Who's next?"
    hide kuviis
    with dissolve

    unknown "I can go next..."
    show bluejay
    with dissolve
    "We all turned to look at the source of the grizzly voice. It was an older man with a bunch of scars on his face."
    bluejay "My name is Eignar, but you can call me Bluejay. I'll be honest, at 58 years old, I'm not really set up for adventuring much these days, so I applied here, hoping that I'd be able to find somewhere calm to retire."
    bluejay "I'm currently classified as 'undecided' for my major, and I'd like to keep it that way."

    "He was a little strange, and you suspected that he was hiding a few things."
    "The silence in the group opened up for the last member of the group to talk."

    hide bluejay
    show ralph
    
    ralph "The name's Ralph Qurnaget, and I'm here studying nature magic as a representative of my clan."
    "The elf spoke somewhat bluntly, although with the typical refinedness that elves usually speak with. It was kind of strange listening to him, to be honest."
    ralph "I'm also the oldest out of all of us, at 312 years old."

    "312?! The elf looked like he was in his 20s! Genetics were truly unfair sometimes."
    "Ralph smiled as he noticed the shock on all of our faces."

    ralph "Well alright then, that's all the introductions for our group, and just in time, it looks like the professor is bringing everyone back together."

    hide ralph
    with dissolve
    "Ralph gestured up to the front of the classroom, to which we all moved our eyes. The professor was indeed standing up and preparing to talk to the class."

    show professor
    professor "Alright, hopefully you've all gotten a chance to meet each other. Now, we're going to talk about the project for the year."

    call project_intro from _call_project_intro

    "After the professor finished his explanation of the project, class ended. My groupmates all bid each other goodbye until tomorrow, and I returned to my room."

    return

label project_intro:
    "Explain the project..."

    return