init python:
    from enum import Enum
    
    class Location(Enum):
        UNKNOWN = "Unknown"
        CLASSROOM = "Classroom"
        DREAM = "Dream"
        DORM = "Dorm"
        BALVOR_TOWER = "Balvor Tower"
        DALORS_FURY = "Dalor's Fury"
        FIGHTERS_GUILD = "Fighter's Guild"
        LILYWATCH = "Lilywatch"
        LOVERS_FOLLY = "Lover's Folly"
        PRAELOR = "Praelor"
        PRAELOR_BRASHY_BREW = "The Brashy Brew"
        TEMPLE_OF_AEYENLO = "Temple of Aeyenlo"
        THE_CITADEL = "The Citadel"
        THE_CITADEL_LIBRARY = "The Library"
        URSIOWATCH = "Ursiowatch"

    class Event_Type(Enum):
        MAIN_STORY_EVENT = 1
        CHARACTER_EVENT = 2

    # For use on the map UI
    def JumpAndHide(target):
        renpy.jump(target)
        renpy.hide_screen("MapUI")

    # Fade between dialogue texts
    def fade_in_callback(who, *args, **kwargs):
        dis = Dissolve(0.5)
        renpy.transition(dis)
        return args, kwargs

    config.say_arguments_callback = fade_in_callback

default dissolve = Fade(2.5, 1, 1)
define flash = Fade(.25, 0.0, .75, color="#fff")
    