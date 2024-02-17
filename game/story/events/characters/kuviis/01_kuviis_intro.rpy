label kuviis_intro:
    # When player enters Lover’s Folly for the first time after meeting the class project teammates
    # show bg lovers_folly_outside panning top to bottom

    "You looked up at the massive lighthouse towering next to the dorms. You weren't really sure why a landlocked academy needed a lighthouse, but certainly the architects in charge of building this place had a reason for it. Maybe you could ask Gudrak sometime."
    "Regardless, you wanted to explore more of the Academy grounds, and of course, that led you right to Lover's Folly."

    show bg lovers_folly_staircase
    "As you stepped into the building, you saw a winding staircase that led to the top of the tower."
    "Not wanting to delay your exploration, you walked up to the top"

    show bg lovers_folly
    "At first glance, it seemed like a normal lighthouse, with not much interesting about it. At a longer glance, you were surprised that one of your group mates was here!"

    # Kuviis leaning on the railing, looking out from the lighthouse at the surroundings
    show bg kuviis_cg_lovers_folly
    "You saw Kuviis leaning on a railing, looking out at the surroundings. She didn't notice you come up, and for a second you didn't want to interrupt her daydreaming."
    "Nevertheless, you thought it would be bad to just stare, and you didn't want to just leave after climbing all those steps to get here…"

    mc "Hey…"

    show bg lovers_folly

    kuviis "KYAA!"

    # show kuviis angry
    kuviis "What are you doing here?! You scared me half to death. First you bumped into me, and now you're sneaking up on me?"
    "You took a deep breath. This girl's arrogance in class, along with her aggressive conduct toward you, to say the least, was making it really hard to decide how to deal with her."

    menu:
        "Should I apologize to her?"

        "Apologize to Kuviis":
            mc "I didn't mean to scare you, I was just exploring, and happened to see you here."
            mc "And hey, I'm sorry about bumping into you earlier, it was genuinely an accident. I was distracted from all the new scenery."
            "Kuviis' face seemed to soften a bit."
            show kuviis
            kuviis "I guess it's ok, I can understand getting distracted. I was pretty distracted looking at the landscape, so I didn't even notice you come up here. That's probably on me."

        "Don't apologize.":
            mc "I didn't mean to scare you! I was just exploring, and happened to see you here."
            "Kuviis' face seemed to soften a bit."
            show kuviis
            "Well, I guess it's not the biggest deal in the world. Everyone is allowed up here, so I should've noticed someone else coming."

    "You couldn't really read her reaction, but at the very least she didn't seem mad anymore."
    mc "Hey, we're group members for the project, I just want to make sure that there's no bad blood between us."

    "Kuviis seemed to ponder for a bit, and then spoke."
    kuviis "I'm not really the type to hold a grudge, so I'll forgive you this time. Just, try to watch where you're going please?"
    "For a second you thought you saw a smirk creep onto her face, however, it was gone almost as soon as it appeared."
    kuviis "And you're right, we're group mates, so we should at least try to be on good terms. Come here, I'll show you what I was looking at."

    hide kuviis

    "You walked up to Kuviis to join her at the railing. You followed her gaze, and the two of you looked at the surrounding landscapes."

    # pan left->right
    show bg lovers_folly_landscapes

    show bg lovers_folly

    kuviis "As soon as I found this place, I kept coming back to look at the beautiful scenery. There's just something about it that seems like it's begging you to come and explore it, and go on some great adventure. After I graduate from this academy, I hope to go do something exciting like that."

    menu:
        "I want to go on an adventure like that one day too.":
            mc "I want to go on an adventure like that one day too."
            
        "I never really saw myself as the adventuring type.":
            mc "I never really saw myself as the adventuring type."

        "Stay silent.":
            mc "..."
    "Kuviis seemed to be lost in thought."
    kuviis "Well, focusing on graduating and this class project should be the first thing on our priority list."

    "Kuviis turned toward you."
    kuviis "Well, I should get going. It was nice talking to you."

    hide kuviis
    "Before you knew it, Kuviis walked down the stairs, leaving you by yourself at the top of the tower."
    "At least things seemed smoothed over with her, but you were hopeful that her fiery temper wasn't going to be a regular appearance."
    "You spent a little longer at Lover's Folly staring at the landscape before deciding to head back."

    return
