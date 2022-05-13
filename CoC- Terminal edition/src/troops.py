import time

class Troop:
    def __init__(self, health, damage, speed, pos):
        # self.name = name
        self.basehealth = health
        self.curhealth = health
        self.damage = damage
        self.speed = speed
        self.pos = pos #pos is a list with x and y coordinates of the king
        self.alive = True

    def get_health(self):
        return (float(self.curhealth) / float(self.basehealth)) * 100

    def got_hit(self, enemy,vmapc):
        self.curhealth -= enemy.damage
        if self.curhealth <= 0:
            self.curhealth = 0
            self.alive = False
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"] = "n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["hover"] = "n"
    
    def do_hit(self, enemy,vmapc):
        enemy.got_hit(self,vmapc)

    def get_coordinates(self):
        return self.pos

class King(Troop):
    
    def __init__(self, health, damage, speed,pos):
        super().__init__(health, damage, speed,pos)
        self.range=2 #change to any value to increase area of attack
    
    def move_up(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]-self.speed
        if(tocheck<0):
            # if(self.pos[0]>0):
            #     tocheck
            tocheck=0
        for i in range(1,self.pos[0]-tocheck+1):
            if(vmapc.vmap[self.pos[0]-i][self.pos[1]]["f"]=="n"):
                continue
            else:
                self.pos[0]=self.pos[0]-i+1
                vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
                return
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
    
    def move_down(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]+self.speed
        if(tocheck>=vmapc.rbound-1):
            # print("tocheck, rbound: ",tocheck,vmapc.rbound)
            tocheck=vmapc.rbound-1
        
        for i in range(1,tocheck-self.pos[0]+1):
            if(vmapc.vmap[self.pos[0]+i][self.pos[1]]["f"]=="n"):
                continue
            else:
                self.pos[0]=self.pos[0]+i-1
                vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
                return
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
        
    
    def move_left(self,vmapc):
        oldpos=self.pos[1]
        tocheck=self.pos[1]-self.speed
        if(tocheck<0):
            tocheck=0

        for i in range(1,self.pos[1]-tocheck+1):
            if(vmapc.vmap[self.pos[0]][self.pos[1]-i]["f"]=="n"):
                continue
            else:
                self.pos[1]=self.pos[1]-i+1
                vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
                return
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
        
    
    def move_right(self,vmapc): 
        oldpos=self.pos[1]
        tocheck=self.pos[1]+self.speed
        if(tocheck>=vmapc.ubound-1):
            tocheck=vmapc.ubound-1
        for i in range(1,tocheck-self.pos[1]+1):
            if(vmapc.vmap[self.pos[0]][self.pos[1]+i]["f"]=="n"):
                continue
            else:
                self.pos[1]=self.pos[1]+i-1
                vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"
                return
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="k"

class Queen(Troop):
    
    def __init__(self, health, damage, speed,pos):
        super().__init__(health, damage, speed,pos)
        self.range=5 #change to any value to increase area of attack
    
    def move_up(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]-self.speed
        if(tocheck<0):
            # if(self.pos[0]>0):
            #     tocheck
            tocheck=0
        for i in range(1,self.pos[0]-tocheck+1):
            if(vmapc.vmap[self.pos[0]-i][self.pos[1]]["f"]=="n"):
                continue
            else:
                self.pos[0]=self.pos[0]-i+1
                vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
                return
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
    
    def move_down(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]+self.speed
        if(tocheck>=vmapc.rbound-1):
            # print("tocheck, rbound: ",tocheck,vmapc.rbound)
            tocheck=vmapc.rbound-1
        
        for i in range(1,tocheck-self.pos[0]+1):
            if(vmapc.vmap[self.pos[0]+i][self.pos[1]]["f"]=="n"):
                continue
            else:
                self.pos[0]=self.pos[0]+i-1
                vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
                return
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
        
    
    def move_left(self,vmapc):
        oldpos=self.pos[1]
        tocheck=self.pos[1]-self.speed
        if(tocheck<0):
            tocheck=0

        for i in range(1,self.pos[1]-tocheck+1):
            if(vmapc.vmap[self.pos[0]][self.pos[1]-i]["f"]=="n"):
                continue
            else:
                self.pos[1]=self.pos[1]-i+1
                vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
                return
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
        
    
    def move_right(self,vmapc): 
        oldpos=self.pos[1]
        tocheck=self.pos[1]+self.speed
        if(tocheck>=vmapc.ubound-1):
            tocheck=vmapc.ubound-1
        for i in range(1,tocheck-self.pos[1]+1):
            if(vmapc.vmap[self.pos[0]][self.pos[1]+i]["f"]=="n"):
                continue
            else:
                self.pos[1]=self.pos[1]+i-1
                vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
                vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"
                return
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="q"

class Barbarian(Troop):
    def __init__(self, health, damage, speed,pos,index):
        super().__init__(health, damage, speed,pos)
        self.range=1
        self.index=index
    
    
    def get_index(self):
        return self.index
        
    def move_up(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]-1
        if(tocheck<0):
            tocheck=0
        # for i in range(1,self.pos[0]-tocheck+1):
        #     if(vmapc.vmap[self.pos[0]-i][self.pos[1]]["f"]=="n"):
        #         continue
        #     else:
        #         self.pos[0]=self.pos[0]-i+1
        #         vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
        #         return
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
            vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
    
    def move_down(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]+1
        if(tocheck>=vmapc.rbound-1):
            tocheck=vmapc.rbound-1
        # for i in range(1,tocheck-self.pos[0]+1):
        #     if(vmapc.vmap[self.pos[0]+i][self.pos[1]]["f"]=="n"):
        #         continue
        #     else:
        #         self.pos[0]=self.pos[0]+i-1
        #         vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
        #         return
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
            vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
    
    def move_left(self,vmapc):
        oldpos=self.pos[1]
        tocheck=self.pos[1]-1
        if(tocheck<0):
            tocheck=0
        # for i in range(1,self.pos[1]-tocheck+1):
        #     if(vmapc.vmap[self.pos[0]][self.pos[1]-i]["f"]=="n"):
        #         continue
        #     else:
        #         self.pos[1]=self.pos[1]-i+1
        #         vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
        #         return
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
            vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
    
    def move_right(self,vmapc): 
        oldpos=self.pos[1]
        tocheck=self.pos[1]+1
        if(tocheck>=vmapc.ubound-1):
            tocheck=vmapc.ubound-1
        # for i in range(1,tocheck-self.pos[1]+1):
        #     if(vmapc.vmap[self.pos[0]][self.pos[1]+i]["f"]=="n"):
        #         continue
        #     else:
        #         self.pos[1]=self.pos[1]+i-1
        #         vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
        #         vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
        #         return
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="b"
            vmapc.vmap[self.pos[0]][self.pos[1]]["b"]=self.index
    
    # barbarian check which is the nearest non-wall building to him
    def check_nearest_building(self,vmapc):
        nearest_building=None
        nearest_building_dist=100
        for i in range(vmapc.rbound):
            for j in range(vmapc.ubound):
                if(vmapc.vmap[i][j]["f"]=="n" or vmapc.vmap[i][j]["f"]=="b" or vmapc.vmap[i][j]["f"]=="k" or vmapc.vmap[i][j]["f"]=="w" or vmapc.vmap[i][j]["f"]=="q"):
                    continue
                else:
                    dist=abs(self.pos[0]-i)+abs(self.pos[1]-j)
                    if(dist<nearest_building_dist):
                        nearest_building_dist=dist
                        bt=vmapc.vmap[i][j]["f"]
                        if(bt=="t"):
                            index=0
                        else:
                            index=vmapc.vmap[i][j][bt]
                        nearest_building=[i,j,bt,index]
        return nearest_building


    def barb_path(self,vmapc,hutlist,townhall,cannonlist,walllist,wizlist):
        if(self.alive==False):
            return
        nearest_building=self.check_nearest_building(vmapc)
        if(nearest_building==None):
            return
        if((self.pos[0]==nearest_building[0]-1 and self.pos[1]==nearest_building[1]) or (self.pos[0]==nearest_building[0]+1 and self.pos[1]==nearest_building[1]) or (self.pos[1]==nearest_building[1]-1 and self.pos[0]==nearest_building[0]) or (self.pos[1]==nearest_building[1]+1 and self.pos[0]==nearest_building[0])):
            # self.pos[0]=nearest_building[0]
            # self.pos[1]=nearest_building[1]
            # vmapc.vmap[self.pos[0]][self.pos[1]][nearest_building[2]]=nearest_building[3]
            # return
            btype=nearest_building[2]
            index=nearest_building[3]
            if(btype=="h"):
                # print("Trying to attck hut at index:",index)
                self.do_hit(hutlist[index],vmapc)
            elif(btype=="t"):
                self.do_hit(townhall,vmapc)
            elif(btype=="c"):
                self.do_hit(cannonlist[index],vmapc)
            elif(btype=="p"):
                self.do_hit(wizlist[index],vmapc)
        else:
            if(self.pos[0]<nearest_building[0]):
                if(vmapc.vmap[self.pos[0]+1][self.pos[1]]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]+1][self.pos[1]]["w"]],vmapc)
                else:
                    self.move_down(vmapc)
            elif(self.pos[0]>nearest_building[0]):
                if(vmapc.vmap[self.pos[0]-1][self.pos[1]]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]-1][self.pos[1]]["w"]],vmapc)
                else:
                    self.move_up(vmapc)
            elif(self.pos[1]<nearest_building[1]):
                if(vmapc.vmap[self.pos[0]][self.pos[1]+1]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]][self.pos[1]+1]["w"]],vmapc)
                else:
                    self.move_right(vmapc)
            elif(self.pos[1]>nearest_building[1]):
                if(vmapc.vmap[self.pos[0]][self.pos[1]-1]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]][self.pos[1]-1]["w"]],vmapc)
                else:
                    self.move_left(vmapc)

# new troop balloon like barbarian that prioritise defensive buildings
class Balloon(Troop):
    def __init__(self, health, damage, speed, pos,index):
        super().__init__(health, damage, speed, pos)
        self.range=1
        self.index=index
    
    def get_index(self):
        return self.index  

    def set_speed(self,speed):
        self.speed=speed

    def move_up(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]-1
        if(tocheck<0):
            tocheck=0
        self.pos[0]=tocheck
        if(vmapc.vmap[oldpos][self.pos[1]]["f"]=="loon"):
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="loon"
        else:
            vmapc.vmap[oldpos][self.pos[1]]["hover"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["hover"]="y"
        
        vmapc.vmap[self.pos[0]][self.pos[1]]["loon"]=self.index
    
    def move_down(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]+1
        if(tocheck>vmapc.rbound-1):
            tocheck=vmapc.rbound-1
        self.pos[0]=tocheck
        if(vmapc.vmap[oldpos][self.pos[1]]["f"]=="loon"):
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="loon"
        else:
            vmapc.vmap[oldpos][self.pos[1]]["hover"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["hover"]="y"
        vmapc.vmap[self.pos[0]][self.pos[1]]["loon"]=self.index
    
    def move_left(self,vmapc):
        oldpos=self.pos[1]
        tocheck=self.pos[1]-1
        if(tocheck<0):
            tocheck=0
        self.pos[1]=tocheck
        if(vmapc.vmap[self.pos[0]][oldpos]["f"]=="loon"):
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="loon"
        else:
            vmapc.vmap[self.pos[0]][oldpos]["hover"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["hover"]="y"
        vmapc.vmap[self.pos[0]][self.pos[1]]["loon"]=self.index
    
    def move_right(self,vmapc):
        oldpos=self.pos[1]
        tocheck=self.pos[1]+1
        if(tocheck>=vmapc.ubound-1):
            tocheck=vmapc.ubound-1
        self.pos[1]=tocheck
        vmapc.vmap[self.pos[0]][oldpos]["hover"]="n"
        vmapc.vmap[self.pos[0]][self.pos[1]]["hover"]="y"
        vmapc.vmap[self.pos[0]][self.pos[1]]["loon"]=self.index
    
    def check_balloon_building(self,vmapc):
        defcount=0
        nearest_building=None
        nearest_building_dist=100
        for i in range(vmapc.rbound):
            for j in range(vmapc.ubound):
                # if(vmapc.vmap[i][j]["f"]=="n" or vmapc.vmap[i][j]["f"]=="b" or vmapc.vmap[i][j]["f"]=="k" or vmapc.vmap[i][j]["f"]=="w" or vmapc.vmap[i][j]["f"]=="q"):

                #     continue
                # else:
                if(vmapc.vmap[i][j]["f"] in ["c","p"]):
                    defcount+=1
                    dist=abs(self.pos[0]-i)+abs(self.pos[1]-j)
                    if(dist<nearest_building_dist):
                        nearest_building_dist=dist
                        bt=vmapc.vmap[i][j]["f"]
                        if(bt=="t"):
                            index=0
                        else:
                            index=vmapc.vmap[i][j][bt]
                        nearest_building=[i,j,bt,index]
                    else:
                        continue
        if(defcount==0):
            for i in range(vmapc.rbound):
                for j in range(vmapc.ubound):
                    if(vmapc.vmap[i][j]["f"] not in ["w","n","k","b","q"]):
                        dist=abs(self.pos[0]-i)+abs(self.pos[1]-j)
                        if(dist<nearest_building_dist):
                            nearest_building_dist=dist
                            bt=vmapc.vmap[i][j]["f"]
                            if(bt=="t"):
                                index=0
                            else:
                                index=vmapc.vmap[i][j][bt]
                            nearest_building=[i,j,bt,index]
        # print("balloon attacking",nearest_building)
        # time.sleep(1)
        return nearest_building
    
    def balloon_path(self,vmapc,hutlist,townhall,cannonlist,wizlist):
        if(self.alive==False):
            vmapc.vmap[self.pos[0]][self.pos[1]]["hover"]="n"
            return
        nearest_building=self.check_balloon_building(vmapc)
        if(nearest_building==None):
            return
        if((self.pos[0]==nearest_building[0]-1 and self.pos[1]==nearest_building[1]) or (self.pos[0]==nearest_building[0]+1 and self.pos[1]==nearest_building[1]) or (self.pos[1]==nearest_building[1]-1 and self.pos[0]==nearest_building[0]) or (self.pos[1]==nearest_building[1]+1 and self.pos[0]==nearest_building[0])):
            btype=nearest_building[2]
            index=nearest_building[3]
            if(btype=="h"):
                # print("Trying to attck hut at index:",index)
                self.do_hit(hutlist[index],vmapc)
            elif(btype=="t"):
                self.do_hit(townhall,vmapc)
            elif(btype=="c"):
                self.do_hit(cannonlist[index],vmapc)
            elif(btype=="p"):
                self.do_hit(wizlist[index],vmapc)
        
        else:
            if(self.pos[0]>nearest_building[0]):
                self.move_up(vmapc)
            elif(self.pos[0]<nearest_building[0]):
                self.move_down(vmapc)
            elif(self.pos[1]>nearest_building[1]):
                self.move_left(vmapc)
            elif(self.pos[1]<nearest_building[1]):
                self.move_right(vmapc)

class Archer(Troop):
    def __init__(self, health, damage, speed,pos,index):
        super().__init__(health, damage, speed,pos)
        self.range=5
        self.index=index
    
    def get_index(self):
        return self.index
    
    def move_up(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]-1
        if(tocheck<0):
            tocheck=0
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            # print("should move up")
            # time.sleep(2)
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="a"
            vmapc.vmap[self.pos[0]][self.pos[1]]["a"]=self.index
    
    def move_down(self,vmapc):
        oldpos=self.pos[0]
        tocheck=self.pos[0]+1
        if(tocheck>=vmapc.rbound-1):
            tocheck=vmapc.rbound-1
        if(vmapc.vmap[tocheck][self.pos[1]]["f"]=="n"):
            self.pos[0]=tocheck
            vmapc.vmap[oldpos][self.pos[1]]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="a"
            vmapc.vmap[self.pos[0]][self.pos[1]]["a"]=self.index
    
    def move_left(self,vmapc):
        oldpos=self.pos[1]
        tocheck=self.pos[1]-1
        if(tocheck<0):
            tocheck=0
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            # print("should move up")
            # time.sleep(2)
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="a"
            vmapc.vmap[self.pos[0]][self.pos[1]]["a"]=self.index
    
    def move_right(self,vmapc): 
        oldpos=self.pos[1]
        tocheck=self.pos[1]+1
        if(tocheck>=vmapc.ubound-1):
            tocheck=vmapc.ubound-1
        if(vmapc.vmap[self.pos[0]][tocheck]["f"]=="n"):
            self.pos[1]=tocheck
            vmapc.vmap[self.pos[0]][oldpos]["f"]="n"
            vmapc.vmap[self.pos[0]][self.pos[1]]["f"]="a"
            vmapc.vmap[self.pos[0]][self.pos[1]]["a"]=self.index
    
    def check_nearest_building(self,vmapc):
        nearest_building=None
        nearest_building_dist=100
        for i in range(vmapc.rbound):
            for j in range(vmapc.ubound):
                # if(vmapc.vmap[i][j]["f"]=="n" or vmapc.vmap[i][j]["f"]=="b" or vmapc.vmap[i][j]["f"]=="k" or vmapc.vmap[i][j]["f"]=="w" or vmapc.vmap[i][j]["f"]=="q"):
                if(vmapc.vmap[i][j]["f"] in ["n","b","k","w","q","a"]):
                    continue
                else:
                    dist=abs(self.pos[0]-i)+abs(self.pos[1]-j)
                    if(dist<nearest_building_dist):
                        nearest_building_dist=dist
                        bt=vmapc.vmap[i][j]["f"]
                        if(bt=="t"):
                            index=0
                        else:
                            index=vmapc.vmap[i][j][bt]
                        nearest_building=[i,j,bt,index]
        return nearest_building
    
    def archer_path(self,vmapc,hutlist,townhall,cannonlist,walllist,wizlist):
        if(self.alive==False):
            return
        nearest_building=self.check_nearest_building(vmapc)
        # print("nearest building:",nearest_building)
        # time.sleep(2)
        if(nearest_building==None):
            # print("no building found")
            # time.sleep(2)
            return
        arange=self.range
        xdist=abs(self.pos[0]-nearest_building[0])
        ydist=abs(self.pos[1]-nearest_building[1])
        # if((self.pos[0]==nearest_building[0]-arange and self.pos[1]==nearest_building[1]) or (self.pos[0]==nearest_building[0]+arange and self.pos[1]==nearest_building[1]) or (self.pos[1]==nearest_building[1]-arange and self.pos[0]==nearest_building[0]) or (self.pos[1]==nearest_building[1]+arange and self.pos[0]==nearest_building[0])):
        # if(self.pos[0] in range(nearest_building[0]-arange,nearest_building[0]+arange+1) or self.pos[1] in range(nearest_building[1]-arange,nearest_building[1]+arange+1)):
        if(max(xdist,ydist)<=arange):
            btype=nearest_building[2]
            index=nearest_building[3]
            if(btype=="h"):
                # print("Trying to attck hut at index:",index)
                # time.sleep(2)
                self.do_hit(hutlist[index],vmapc)
            elif(btype=="t"):
                # print("townhall")
                # time.sleep(2)
                self.do_hit(townhall,vmapc)
            elif(btype=="c"):
                # print("cannon")
                # time.sleep(2)
                self.do_hit(cannonlist[index],vmapc)
            elif(btype=="p"):
                # print("wiztower")
                # time.sleep(2)
                self.do_hit(wizlist[index],vmapc)

        else:
            if(self.pos[0]<nearest_building[0]):
                if(vmapc.vmap[self.pos[0]+1][self.pos[1]]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]+1][self.pos[1]]["w"]],vmapc)
                else:
                    self.move_down(vmapc)
            elif(self.pos[0]>nearest_building[0]):
                if(vmapc.vmap[self.pos[0]-1][self.pos[1]]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]-1][self.pos[1]]["w"]],vmapc)
                else:
                    self.move_up(vmapc)
            elif(self.pos[1]<nearest_building[1]):
                if(vmapc.vmap[self.pos[0]][self.pos[1]+1]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]][self.pos[1]+1]["w"]],vmapc)
                else:
                    self.move_right(vmapc)
            elif(self.pos[1]>nearest_building[1]):
                if(vmapc.vmap[self.pos[0]][self.pos[1]-1]["f"]=="w"):
                    self.do_hit(walllist[vmapc.vmap[self.pos[0]][self.pos[1]-1]["w"]],vmapc)
                else:
                    self.move_left(vmapc)