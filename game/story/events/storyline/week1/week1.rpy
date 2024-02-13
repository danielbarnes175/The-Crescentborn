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