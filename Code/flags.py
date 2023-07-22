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

class CircumstanceComplexityModifiers(Flag):
    NONE = auto()
    LOCATION_LEYLINE_ALIGNS = auto()
    LOCATION_LEYLINE_OPPOSES = auto()
    WEATHER_ALIGNMENT = auto()
    TIME_ALIGNMENT = auto()
    RITUAL_OPPOSES_NATURE = auto()
    THREE_FOLD_COMPONENT_SYMMETRY = auto()
    FIVE_FOLD_COMPONENT_SYMETRY = auto()
    LIFE_ON_THE_LINE = auto()

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