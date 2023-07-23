from ritualObject import RitualObject
from flags import TypesOfTime, CircumstanceComplexityModifiers

class Ritual():
    def __init__(self):
        self.creationCheck = "Occult"
        self.creationDifficulty = 0
        self.creationCheck = 0

        self.performingCheck = "None"
        self.performingDifficulty = 0
        self.performingCheck = 0

        self.typeOfTimeDevoted = TypesOfTime.NONE
        self.timeSpentCheckModifier = 0
        self.ritualObjects = []

        self.circumstanceComplexityModifiers = CircumstanceComplexityModifiers.NONE
        self.circumstanceLocationLeylineValue = 0.0
        self.circumstanceWeatherValue = 0
        self.circumstanceTimeValue = 0
        self.circumstanceRitualNatureValue = 0
        self.circumstanceThreeFoldSymmetryValue = 0.0
        self.circumstanceFiveFoldSymmetryValue = 0.0
        self.circumstanceLifeOnTheLineValue = 0

        self.cirumstancePercentageModifiersFinalValue = 0.0
        self.circumstanceFlatModifiersFinalValue = 0

        print("Ritual is created")

    def addRitualObject(self, ritualObject: RitualObject):
        if (isinstance(ritualObject, RitualObject) == False):
            print("ERROR: Didn't recieve RitualObject Object")
            return
        
        self.ritualObjects.append(ritualObject)

    # This will be applied for the performing of the ritual
    def checkComplexityModifierValues(self):
        print("a")
        if (CircumstanceComplexityModifiers.LOCATION_LEYLINE_ALIGNS in self.circumstanceComplexityModifiers):
            if (self.circumstanceLocationLeylineValue < -0.25):
                self.circumstanceLocationLeylineValue = -0.25
            elif (self.circumstanceLocationLeylineValue > -0.01):
                self.circumstanceLocationLeylineValue = -0.01
        
        if (CircumstanceComplexityModifiers.LOCATION_LEYLINE_OPPOSES in self.circumstanceComplexityModifiers):
            if (self.circumstanceLocationLeylineValue > 1.00):
                self.circumstanceLocationLeylineValue = 1.00
            elif (self.circumstanceLocationLeylineValue < 0.01):
                self.circumstanceLocationLeylineValue = 0.01

        if (CircumstanceComplexityModifiers.WEATHER_ALIGNMENT in self.circumstanceComplexityModifiers):
            if (self.circumstanceWeatherValue < -75):
                self.circumstanceWeatherValue = -75
            elif (self.circumstanceWeatherValue > 75):
                self.circumstanceWeatherValue = 75

        if (CircumstanceComplexityModifiers.TIME_ALIGNMENT in self.circumstanceComplexityModifiers):
            if (self.circumstanceTimeValue < -15):
                self.circumstanceTimeValue = -15
            elif (self.circumstanceTimeValue > 15):
                self.circumstanceTimeValue = 15

        if (CircumstanceComplexityModifiers.RITUAL_OPPOSES_NATURE in self.circumstanceComplexityModifiers):
            if (self.circumstanceRitualNatureValue < 5):
                self.circumstanceRitualNatureValue = 5
            elif (self.circumstanceRitualNatureValue > 50):
                self.circumstanceRitualNatureValue = 50

        if (CircumstanceComplexityModifiers.THREE_FOLD_COMPONENT_SYMMETRY in self.circumstanceComplexityModifiers):
            # cuidao que es un float
            if (self.circumstanceThreeFoldSymmetryValue < -0.30):
                self.circumstanceThreeFoldSymmetryValue = -0.30
            elif (self.circumstanceThreeFoldSymmetryValue > -0.30):
                self.circumstanceThreeFoldSymmetryValue = -0.30

        if (CircumstanceComplexityModifiers.FIVE_FOLD_COMPONENT_SYMETRY in self.circumstanceComplexityModifiers):
            # cuidao que es un float
            if (self.circumstanceFiveFoldSymmetryValue < -0.50):
                self.circumstanceFiveFoldSymmetryValue = -0.50
            elif (self.circumstanceFiveFoldSymmetryValue > -0.50):
                self.circumstanceFiveFoldSymmetryValue = -0.50
        
        if (CircumstanceComplexityModifiers.LIFE_ON_THE_LINE in self.circumstanceComplexityModifiers):
            if (self.circumstanceLifeOnTheLineValue != -10):
                self.circumstanceLifeOnTheLineValue = -10
    
    # This will be applied to the creation of the ritual
    def timeSpentModifierCalculation(self, amount: int):
        if (isinstance(amount, int) == False):
            print("ERROR: Invalid input, insert number")
            return

        match self.typeOfTimeDevoted:
            case TypesOfTime.SECONDS:
                self.timeSpentCheckModifier = -30
            
            case TypesOfTime.MINUTES:
                self.timeSpentCheckModifier = -24 + (1*(amount/5))

            case TypesOfTime.HOURS:
                self.timeSpentCheckModifier = 0 + (1*(amount/5))
            
            case TypesOfTime.DAYS:
                self.timeSpentCheckModifier = 5 + (5*amount)

            case TypesOfTime.WEEKS:
                self.timeSpentCheckModifier = 35 + (5*amount)

            case TypesOfTime.MONTHS:
                self.timeSpentCheckModifier = 50 + (5*amount)

            case TypesOfTime.YEARS:
                self.timeSpentCheckModifier = 110 + (25*amount)

            case TypesOfTime.LIFETIMES:
                self.timeSpentCheckModifier = 1000 + (150*amount)

            case default:
                self.timeSpentCheckModifier = 0
                print("enters in default")

    def printTest(self):
        print(self.creationCheck)
        self.typeOfTimeDevoted = TypesOfTime.SECONDS
        self.timeSpentModifierCalculation(5)
        self.circumstanceComplexityModifiers = CircumstanceComplexityModifiers.TIME_ALIGNMENT | CircumstanceComplexityModifiers.LOCATION_LEYLINE_ALIGNS
        self.checkComplexityModifierValues()
        print("ritual print successful")