# class for buildings

class Building:
    def __init__(self,hp,ar,type):
        self.basehitpoints=hp
        self.curhitpoints=hp
        self.coords=ar #area is a list with x and y span of the building
        self.toshow=True
        self.type=type
    
    def get_hp(self):
        return (float(self.curhitpoints)/float(self.basehitpoints))*100
    
    def get_coordinates(self):
        return self.coords

    def got_hit(self,troop,vmapc):
        self.curhitpoints-=troop.damage
        if self.curhitpoints<=0:
            if(self.type!="w"):
                vmapc.curbuild-=1
                vmapc.curbuildhp-=self.basehitpoints
            self.curhitpoints=0
            self.toshow=False
            if(self.type!="t"):
                vmapc.vmap[self.coords[0]][self.coords[1]]["f"]="n"
            else:
                for i in range(3):
                    for j in range(4):
                        vmapc.vmap[self.coords[0]-i][self.coords[1]+j]["f"]="n"

class Wall(Building):
    def __init__(self,hp,ar,type):
        super().__init__(hp,ar,"w")
    # def draw_wall(self,x,y):
    #     if self.toshow==True:
    #         print("\033[{};{}H#".format(y,x))


# townhall class
class Townhall(Building):    
    def _init_(self,hp,ar,type):
        super().__init__(hp,ar,"t")
    #     Building.__init__(self,hp,ar)

class Hut(Building):
    def __init__(self,hp,ar,type):
        super().__init__(hp,ar,"h")

class Cannon(Building):
    def __init__(self,hp,ar,dmg,type):
        super().__init__(hp,ar,"c")
        self.damage=dmg
        self.flashing=False
        self.flashingcount=0
    
    def set_flashing(self,flashing):
        self.flashing=flashing
    def shoot(self,troop,vmapc):
        troop.got_hit(self,vmapc)
    def toshoot(self,troop,vmapc):
        if(self.toshow==True):
            mindist=max(abs(troop.pos[0]-self.coords[0]),abs(troop.pos[1]-self.coords[1]))
            if mindist<=6:
                # self.flashing=True
                self.set_flashing(True)
                if(self.flashingcount==0):
                    self.flashingcount=1
                else:
                    self.flashingcount=0
                self.shoot(troop,vmapc)
            else:
                # self.flashing=False
                self.set_flashing(False)
                self.flashingcount=0
    def canshoot(self,troop):
        if(self.toshow==True):
            mindist=max(abs(troop.pos[0]-self.coords[0]),abs(troop.pos[1]-self.coords[1]))
            if mindist<=6:
                # self.flashing=True
                # self.set_flashing(True)
                # if(self.flashingcount==0):
                #     self.flashingcount=1
                # else:
                #     self.flashingcount=0
                # self.shoot(troop,vmapc)
                return True
            else:
                self.flashing=False
                self.set_flashing(False)
                self.flashingcount=0
                return False
    def get_flashing(self):
        return self.flashing
    def get_flashingcount(self):
        return self.flashingcount


#class for wizard tower
class Wizardtower(Building):
    def __init__(self,hp,ar,dmg,type):
        super().__init__(hp,ar,"p")
        self.damage=dmg
        self.flashing=False
    
    # def getaffectedtroops(self,troop,vmapc):
    #     trooplist=[]

    def set_flashing(self,flashing):
        self.flashing=flashing
    def get_flashing(self):
        return self.flashing

    def canshoot(self,trooplist):
        # coords=[]
        if(self.toshow==True):
            # for troop in trooplist:
            for i in range(len(trooplist)):
                troop=trooplist[i]
                if(troop.alive==False):
                    continue
                mindist=max(abs(troop.pos[0]-self.coords[0]),abs(troop.pos[1]-self.coords[1]))
                if mindist<=6:
                    self.flashing=True
                    # self.shoot(troop,vmapc)
                    return troop.pos
                else:
                    self.flashing=False
                    # return False
        return [-1,-1]

    def shoot(self,trooplist,vmapc):
        for troop in trooplist:
            troop.got_hit(self,vmapc)
    
    # def toshoot(self,troop,vmapc):
    #     self.shoot(troop,vmapc)
        # if(self.toshow==True):
            # mindist=max(abs(troop.pos[0]-self.coords[0]),abs(troop.pos[1]-self.coords[1]))
            # if mindist<=6:
                # self.shoot(troop,vmapc)
            #     trooplist=self.getaffectedtroops(troop,vmapc,mindist)
            #     self.flashing=True
            # else:
            #     self.flashing=False

     

