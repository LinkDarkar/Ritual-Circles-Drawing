from enum import Flag, auto

class TypesOfTime(Flag):
    NONE = auto()
    SECONDS = auto()    # considered as "in-combat" preparation
    MINUTES = auto()
    HOURS = auto()
    DAYS = auto()
    WEEKS = auto()
    MONTHS = auto()
    YEARS = auto()
    LIFETIMES = auto()

class ComponentClass(Flag):
    NONE = auto()
    QUINTESSENCE = auto()
    AUGMENT = auto()
    STRUCTURE = auto()
    UTILITY = auto()

class Intensity(Flag):
    # check if this works correctly
    NONE = auto()
    HEAT = auto()
    COLD = auto()
    ELECTRICITY = auto()