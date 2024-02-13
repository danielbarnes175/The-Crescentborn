init python:
    from enum import Enum
    
    class Location(Enum):
        UNKNOWN = "Unknown"
        CLASSROOM = "Classroom"
        DREAM = "Dream"
        DORM = "Dorm"
        BALVORS_TOWER = "Balvor's Tower"
        DALORS_FURY = "Dalor's Fury"
        FIGHTERS_GUILD = "Fighter's Guild"
        LILYWATCH = "Lilywatch"
        LOVERS_FOLLY = "Lover's Folly"
        PRAELOR = "Praelor"
        TEMPLE_OF_AEYENLO = "Temple of Aeyenlo"
        THE_CITADEL = "The Citadel"
        URSIOWATCH = "Ursiowatch"

    class Event_Type(Enum):
        MAIN_STORY_EVENT = 1
        CHARACTER_EVENT = 2

    # For use on the map UI
    def JumpAndHide(target):
        renpy.jump(target)
        renpy.hide_screen("MapUI")