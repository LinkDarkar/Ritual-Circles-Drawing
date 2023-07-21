from ritualObject import RitualObject
from flags import TypesOfTime

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

        print("Ritual is created")

    def addRitualObject(self, ritualObject=RitualObject):
        if (isinstance(ritualObject, RitualObject) == False):
            # checks if the object recieved is the object wanted, since the program seems to
            # continue even if we give it an integer
            # is this really useful? I guess it could be fine but wouldn't 
            # it be exhausting to have that everytime we give it something?
            print("ERROR: Didn't recieve RitualObject Object")
            return
        self.ritualObjects.append(ritualObject)

    def printTest(self):
        print(self.creationCheck)
        print("ritual print successful")
    
    # This will be applied to the creation of the ritual
    def timeSpentModifierCalculation(self, amount=int):
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

    # This will be applied for the performing of the ritual
    def complexityModifierCalculation(self):
        print("a")