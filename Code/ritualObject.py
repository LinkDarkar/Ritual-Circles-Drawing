class RitualObject():
    def __init__(self):
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