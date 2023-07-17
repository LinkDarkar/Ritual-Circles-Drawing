class RitualObject():
    def __init__(self):
        self.name = "None"
        self.typeOfObject = "None"          # Can be either a weapon, spell, or whatever the fuck it needs to be, wouldn't it be nice for the user to be able to add or delete the types that they wanted and then select them from a menu?
        self.descriptionOfEffect = "None"
        self.complexityModifier = 0
        print("RitualObject is created")

    def printTest(self):
        print(self.descriptionOfEffect)
        print("ritualObject print successful")

# If they end up getting fucked up I'll put them in their own files
# tho I still haven't read enough to be sure if they actually need
# different functions
class RitualObjectStructure(RitualObject):
    pass

class RitualObjectQuintessence(RitualObject):
    pass

class RitualObjectAugment(RitualObject):
    pass

class RitualObjectUtility(RitualObject):
    pass