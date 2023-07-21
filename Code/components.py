from flags import ComponentClass, Intensity

class Component():
    def __init__(self):
        self.description = "None"
        self.image = None
        self.componentClass = ComponentClass.NONE

class ComponentMaterial(Component):
    def __init__(self):
        Component.__init__()
        self.presence = 0

class ComponentMystical(Component):
    def __init__(self, physical, zeon):
        Component.__init__()
        self.presence = 0
        if (physical):
            # ?????????????
            self.complexity = self.presence
        elif (physical == False):
            self.complexity = zeon

class ComponentSpell(Component):
    def __init__(self, zeon):
        Component.__init__()
        self.form = "None"
        self.complexity = zeon

class ComponentSecondarySkill(Component):
    def __init__(self):
        Component.__init__()
        self.form = "None"
        self.isPhysical = False
        self.secondaryAbilityResult = 0

class ComponentElemental(Component):
    def __init__(self):
        Component.__init__()
        self.intensityType = Intensity.NONE
        self.intensityValue = 0


class ComponentRitualSpell(Component):
    def __init__(self):
        Component.__init__()
        self.complexityByClass = 0

class ComponentRitualSpellChannel(ComponentRitualSpell):
    def __init__(self):
        ComponentRitualSpell.__init__()
        match self.componentClass:
            case ComponentClass.QUINTESSENCE:
                self.complexityByClass = 20
            
            case ComponentClass.AUGMENT:
                self.complexityByClass = 10

            case ComponentClass.STRUCTURE:
                self.complexityByClass = 0
            
            case ComponentClass.UTILITY:
                self.complexityByClass = 10

            case default:
                self.complexityByClass = 0

class ComponentRitualSpellTrigger(ComponentRitualSpell):
    def __init__(self):
        ComponentRitualSpell.__init__()
        match self.componentClass:
            case ComponentClass.QUINTESSENCE:
                self.complexityByClass = 20
            
            case ComponentClass.AUGMENT:
                self.complexityByClass = 5

            case ComponentClass.STRUCTURE:
                self.complexityByClass = 5
            
            case ComponentClass.UTILITY:
                self.complexityByClass = 10

            case default:
                self.complexityByClass = 0

class ComponentRitualSpellBalance(ComponentRitualSpell):
    def __init__(self):
        ComponentRitualSpell.__init__()
        match self.componentClass:
            case ComponentClass.QUINTESSENCE:
                self.complexityByClass = 30
            
            case ComponentClass.AUGMENT:
                self.complexityByClass = 5

            case ComponentClass.STRUCTURE:
                self.complexityByClass = -10
            
            case ComponentClass.UTILITY:
                self.complexityByClass = 0

            case default:
                self.complexityByClass = 0

class ComponentRitualSpellAlteration(ComponentRitualSpell):
    def __init__(self):
        ComponentRitualSpell.__init__()
        match self.componentClass:
            case ComponentClass.QUINTESSENCE:
                self.complexityByClass = 50
            
            case ComponentClass.AUGMENT:
                self.complexityByClass = 20

            case ComponentClass.STRUCTURE:
                self.complexityByClass = 40
            
            case ComponentClass.UTILITY:
                self.complexityByClass = 20

            case default:
                self.complexityByClass = 0