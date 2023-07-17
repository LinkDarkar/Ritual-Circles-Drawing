from ritualObject import RitualObject
class Ritual():
    def __init__(self):
        self.typeOfCheck = "None"
        self.timeDevoted = 0
        self.activatingDifficulty = 0
        self.activatingCheck = 0
        self.ritualObjects = []
        print("Ritual is created")

    def addRitualObject(self, ritualObject=RitualObject):
        if (isinstance(ritualObject, RitualObject) == False):
            # checks if the object recieved is the object wanted, since the program seems to
            # continue even if we give it an integer
            # is this really useful? I guess it could be fine but wouldn't 
            # it be exhausting to have that everytime we give it something?
            print("ERROR: Didn't gave RitualObject Object")
            return
        self.ritualObjects.append(ritualObject)

    def printTest(self):
        print(self.typeOfCheck)
        print("ritual print successful")