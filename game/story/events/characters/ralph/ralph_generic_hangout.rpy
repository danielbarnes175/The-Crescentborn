label ralph_generic_hangout:
    $ ralph_generic_hangout.triggered = True
    $ audio_crossFade(2, audio_main_ralph)
    "You hung out with Ralph for a bit, and felt yourself get closer."
    $ audio_crossFade(2, audio_main_free_time)
    return