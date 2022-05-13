class spell:
    def __init__(self,type):
        self.type=type

class healspell(spell):
    def __init__(self,type):
        super().__init__(type)
    
    def activateheal(self,trooplist):
        for i in trooplist:
            nhealthtest=(i.curhealth)*1.5
            if(nhealthtest>i.basehealth):
                i.curhealth=i.basehealth
            else:
                i.curhealth=nhealthtest

class ragespell(spell):
    def __init__(self,type):
        super().__init__(type)
    
    def activaterage(self,trooplist):
        for i in trooplist:
            i.damage*=2
            i.speed*=2