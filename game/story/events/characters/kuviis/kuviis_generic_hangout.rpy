label kuviis_generic_hangout:
    $ kuviis_generic_hangout.triggered = True
    $ audio_crossFade(2, audio_main_kuviis)
    "You hung out with Kuviis for a bit, and felt yourself get closer."
    $ audio_crossFade(2, audio_main_free_time)

    return