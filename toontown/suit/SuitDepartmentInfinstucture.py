from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals, TTLocalizer
import random

class SuitDepartmentBase:
    DEPARTMENT_SHORT_HAND = "v"
    DEPARTMENT_NAME = "Cogbot"
    DEPARTMENT_NAME_PLURAL = "Cogbots"
    DEPARTMENT_NAME_SINGULAR = "a Cogbot"
    DEPARTMENT_CLOTHING_PREFIX = "_v"
    DEPARTMENT_EMPLOYEES = ["t",
                            't',
                            't',
                            't',
                            't',
                            't',
                            't',
                            't']
    DEPARTMENT_MAX_EMPLOYEES = 8
    DEPARTMENT_EMPLOYEE_DESCRIPTIONS = ["A cogbot that is a level 1.",
                                        "A cogbot that is a level 2.",
                                        "A cogbot that is a level 3.",
                                        "A cogbot that is a level 4.",
                                        "A cogbot that is a level 5.",
                                        "A cogbot that is a level 6.",
                                        "A cogbot that is a level 7.",
                                        "A cogbot that is a level 8."]
    
    def __init__(self):
        self.description = "Chainsaw mam, the last laff."
        self.score = "COG RESOURCES SCRORE: MYYYY, MOOOOM!!!! STARLAAAAAAA!!!!"
        self.departmentIdeals = "To destroy all toons and take over the world HHHAHAHAHAHAHAHAH."
    
    def pickRandomSuit(self):
        return random.choice(self.DEPARTMENT_EMPLOYEES)
    
    def checkIfSuitInDepartment(self, suitName):
        return suitName in self.DEPARTMENT_EMPLOYEES

class SuitDepartmentSales(SuitDepartmentBase):
    DEPARTMENT_SHORT_HAND = "s"
    DEPARTMENT_NAME = "Sellbot"
    DEPARTMENT_NAME_PLURAL = "Sellbots"
    DEPARTMENT_NAME_SINGULAR = "a Sellbot"
    DEPARTMENT_CLOTHING_PREFIX = "_s"
    DEPARTMENT_EMPLOYEES = ["cc",
                            'tm',
                            'nd',
                            'gh',
                            'ms',
                            'tf',
                            'm',
                            'mh']
    DEPARTMENT_MAX_EMPLOYEES = 8
    DEPARTMENT_EMPLOYEE_DESCRIPTIONS = ["",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        ""]
    
    def __init__(self):
        SuitDepartmentBase.__init__(self)
        self.description = "The front end customer to pruduction, the roaring 20's of C.O.G.S Inc..."
        self.score = "COG RESOURCES SCRORE: 20*5%"
        self.departmentIdeals = "With any production of your every day cog item, the Factory as you covered. And if your up for the peak of these sleezy sales men, tip-tap-toe to their Sellbot Towers."

class SuitDepartmentBanking(SuitDepartmentBase):
    DEPARTMENT_SHORT_HAND = "m"
    DEPARTMENT_NAME = "Cashbot"
    DEPARTMENT_NAME_PLURAL = "Cashbots"
    DEPARTMENT_NAME_SINGULAR = "a Cashbot"
    DEPARTMENT_CLOTHING_PREFIX = "_m"
    DEPARTMENT_EMPLOYEES = ["sc",
                            'pp',
                            'tw',
                            'bc',
                            'nc',
                            'mb',
                            'ls',
                            'rb']
    DEPARTMENT_MAX_EMPLOYEES = 8
    DEPARTMENT_EMPLOYEE_DESCRIPTIONS = ["",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        ""]
    
    def __init__(self):
        SuitDepartmentBase.__init__(self)
        self.description = "The back-end Vault and Banking Management of C.O.G.S Inc..."
        self.score = "COG RESOURCES SCRORE: 92%"
        self.departmentIdeals = "Your Cold Hard Cash is safe with their department, and if you want to see the peak of their banking system, visit the Cashbot Mints, Supervised by their C.F.O."

class SuitDepartmentLegal(SuitDepartmentBase):
    DEPARTMENT_SHORT_HAND = "l"
    DEPARTMENT_NAME = "Lawbot"
    DEPARTMENT_NAME_PLURAL = "Lawbots"
    DEPARTMENT_NAME_SINGULAR = "a Lawbot"
    DEPARTMENT_CLOTHING_PREFIX = "_l"
    DEPARTMENT_EMPLOYEES = ["bf",
                            'b',
                            'dt',
                            'ac',
                            'bs',
                            'sd',
                            'le',
                            'bw']
    DEPARTMENT_MAX_EMPLOYEES = 8
    DEPARTMENT_EMPLOYEE_DESCRIPTIONS = ["",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        ""]
    
    def __init__(self):
        SuitDepartmentBase.__init__(self)
        self.description = "The Justice of C.O.G.S Inc..."
        self.score = "COG RESOURCES SCRORE: 100%"
        self.departmentIdeals = "The Lawbot Department is the most powerful department for justice for all cogs of C.O.G.S Inc. They are the ones who make the rules, and if you want to see the peak of their justice system, visit the Lawbot Courthouse, Supervised by their C.J."

class SuitDepartmentCorporate(SuitDepartmentBase):
    DEPARTMENT_SHORT_HAND = "c"
    DEPARTMENT_NAME = "Bossbot"
    DEPARTMENT_NAME_PLURAL = "Bossbots"
    DEPARTMENT_NAME_SINGULAR = "a Bossbot"
    DEPARTMENT_CLOTHING_PREFIX = "_c"
    DEPARTMENT_EMPLOYEES = ["f",
                            'p',
                            'ym',
                            'mm',
                            'ds',
                            'hh',
                            'cr',
                            'tbc']
    DEPARTMENT_MAX_EMPLOYEES = 8
    DEPARTMENT_EMPLOYEE_DESCRIPTIONS = ["",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        ""]
    
    def __init__(self):
        SuitDepartmentBase.__init__(self)
        self.description = "The Boss of C.O.G.S Inc..."
        self.score = "COG RESOURCES SCRORE: 100%"
        self.departmentIdeals = "The Bossbot Department is the most powerful department for the Boss of C.O.G.S Inc. They are the ones who call the shots of the corporate side, and if you want to see the peak of their management, visit the Bossbot Clubhouse, Supervised by their C.E.O."

class SuitDepartmentTechnical(SuitDepartmentBase):
    DEPARTMENT_SHORT_HAND = "t"
    DEPARTMENT_NAME = "Techbot"
    DEPARTMENT_NAME_PLURAL = "Techbots"
    DEPARTMENT_NAME_SINGULAR = "a Techbot"
    DEPARTMENT_CLOTHING_PREFIX = "_t"
    DEPARTMENT_EMPLOYEES = ["sk",
                            'cm',
                            'vp',
                            'sdb',
                            'kw',
                            'pyc',
                            'iw',
                            'ru']
    DEPARTMENT_MAX_EMPLOYEES = 8
    DEPARTMENT_EMPLOYEE_DESCRIPTIONS = ["",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        "",
                                        ""]
    
    def __init__(self):
        SuitDepartmentBase.__init__(self)
        self.description = "The Technical Advancements of C.O.G.S Inc..."
        self.score = "COG RESOURCES SCRORE: 100%"
        self.departmentIdeals = "The Techbot Department is the most powerful department for the Technical Advancements of C.O.G.S Inc. They are the ones who make the advancements, and if you want to see the peak of their advancements, visit their Server Room and their Wide Web Office, Supervised by their C.I.O."
