#make coc game using colorama and the classes defined earlier
import sys
from os import system,getcwd
# import os
cwd=getcwd()
cwd+="/src"
# sys.path.insert(1,'/src')
# print(cwd)
sys.path.append(cwd)

from input import *
from colorama import Fore, Back, Style
import troops
import buildings
from village import villagemap
from render import render
from gettargets import *
from level1 import getl1map
from level2 import getl2map
from level3 import getl3map

import time
import spell
import datetime



def allded(trooplist):
    for i in trooplist:
        if(i.alive==True):
            return False
    return True



# print(villmapc.vmap[7][20]["f"])
# c=input("Select k for king and q for queen\n")

heal=spell.healspell("h")
rage=spell.ragespell("r")
filename=sys.argv[1]
# filename="replays/"
# filename+=datetime.datetime.now().strftime("%m-%d-%H-%M-%S")
# filename+=".txt"
f=open(filename,"r")

c=f.read(1)

spawnsite1=[24,49] #barb
spawnsite2=[24,0]
spawnsite3=[0,49]
spawnsite4=[24,16] #loon
spawnsite5=[0,16]
spawnsite6=[16,30]
spawnsite7=[34,99]
spawnsite8=[34,0]
spawnsite9=[0,99]

curlevel=1
while(curlevel<=3):
    if(curlevel==1):
        villmapc,vmap,hutlist,cannonlist,walllist,wizlist,townhall=getl1map()
    elif(curlevel==2):
        villmapc,vmap,hutlist,cannonlist,walllist,wizlist,townhall=getl2map()
    else:
        villmapc,vmap,hutlist,cannonlist,walllist,wizlist,townhall=getl3map()
        # exit(0)
    if(c=="k"):
        Bk=troops.King(2000,50,1,[0,0])
        vmap[0][0]["f"]="k"
    elif(c=="q"):
        Aq=troops.Queen(1000,30,1,[24,0])
        vmap[24][0]["f"]="q"
    else:
        print("Invalid input")
        exit(0)
    bcount=0
    barblist=[]
    lcount=0
    loonlist=[]
    archcount=0
    archlist=[]
    if(c=="k"):
        trooplist=[Bk]
    else:
        trooplist=[Aq]

    longatkpressed=0
    oldlist=[]
    while 1:
        print("buildings left:",villmapc.curbuild)
        # if Bk.alive==False:
        #     print("Game Over")
        #     break
        if(longatkpressed==1 and c=="q"):
            for i in oldlist:
                Aq.do_hit(i,villmapc)
            longatkpressed=0
        if(allded(trooplist)):
            print("Game Over")
            break
        if villmapc.curbuild==0:
            # print("Victory!")
            system("clear")
            if(curlevel!=3):
                print("Level ",curlevel," Victory!")
                print("Going to level ",curlevel+1)
                time.sleep(2)
            curlevel+=1
            break
        # char=input_to()
        char=f.read(1)


        # f.write(char)


        if char=="w" or char=="W":
            if(c=="k"):
                if(Bk.alive):
                    Bk.move_up(villmapc)
            else:
                if(Aq.alive):
                    Aq.move_up(villmapc)
                    curdir="w"
        elif char=="s" or char=="S":
            if(c=="k"):
                if(Bk.alive):
                    Bk.move_down(villmapc)
            else:
                if(Aq.alive):
                    Aq.move_down(villmapc)
                    curdir="s"
        elif char=="a" or char=="A":
            if(c=="k"):
                if(Bk.alive):
                    Bk.move_left(villmapc)
            else:
                if(Aq.alive):
                    Aq.move_left(villmapc)
                    curdir="a"
        elif char=="d" or char=="D":
            if(c=="k"):
                if(Bk.alive):
                    Bk.move_right(villmapc)
            else:
                if(Aq.alive):
                    Aq.move_right(villmapc)
                    curdir="d"

        elif char==" ":
            if(c=="k"):
                buildlist=getbklist(Bk,villmapc,hutlist,walllist,townhall,cannonlist,wizlist)
                for i in buildlist:
                    Bk.do_hit(i,villmapc)
            else:
                buildlist=getaqlist(Aq,villmapc,hutlist,walllist,townhall,cannonlist,curdir,wizlist)
                for i in buildlist:
                    Aq.do_hit(i,villmapc)
        elif char=="x":
            if(c=="q"):
                bigaqlist=getaqbiglist(Aq,villmapc,hutlist,walllist,townhall,cannonlist,curdir,wizlist)
                oldlist=bigaqlist
                longatkpressed=1
                # for i in bigaqlist:
                #     Aq.do_hit(i,villmapc)
        elif char=="h" or char=="H":
            heal.activateheal(trooplist)
        elif char=="r" or char=="R":
            rage.activaterage(trooplist)
        elif char=="q" or char=="Q":
            # break
            exit(0)
        elif char=="1":
            if(bcount>=10):
                print("Barbarian limited to 10")
                # continue
            #release a barbarian on spawnsite 1
            else:
                barb=troops.Barbarian(100,10,1,[spawnsite1[0],spawnsite1[1]],len(barblist))
                barblist.append(barb)
                trooplist.append(barb)
                vmap[spawnsite1[0]][spawnsite1[1]]["f"]="b"
                vmap[spawnsite1[0]][spawnsite1[1]]["b"]=barb.get_index()
                bcount+=1
        
        elif char=="2":
            if(bcount>=10):
                print("Barbarian limited to 10")
            else:
            #release a barbarian on spawnsite 2
                barb=troops.Barbarian(100,10,1,[spawnsite2[0],spawnsite2[1]],len(barblist))
                barblist.append(barb)
                trooplist.append(barb)
                vmap[spawnsite2[0]][spawnsite2[1]]["f"]="b"
                vmap[spawnsite2[0]][spawnsite2[1]]["b"]=barb.get_index()
                bcount+=1
        
        elif char=="3":
            if(bcount>=10):
                print("Barbarian limited to 10")
            #release a barbarian on spawnsite 3
            else:
                barb=troops.Barbarian(100,10,1,[spawnsite3[0],spawnsite3[1]],len(barblist))
                barblist.append(barb)
                trooplist.append(barb)
                vmap[spawnsite3[0]][spawnsite3[1]]["f"]="b"
                vmap[spawnsite3[0]][spawnsite3[1]]["b"]=barb.get_index()
                bcount+=1
        elif char=="4":
            if(lcount>=10):
                print("Balloon limited to 10")
            else:
                loon=troops.Balloon(100,20,2,[spawnsite4[0],spawnsite4[1]],len(loonlist))
                loonlist.append(loon)
                trooplist.append(loon)
                vmap[spawnsite4[0]][spawnsite4[1]]["hover"]="y"
                vmap[spawnsite4[0]][spawnsite4[1]]["loon"]=loon.get_index()
                lcount+=1
        elif char=="5":
            if(lcount>=10):
                print("Balloon limited to 10")
            else:
                loon=troops.Balloon(100,20,2,[spawnsite5[0],spawnsite5[1]],len(loonlist))
                loonlist.append(loon)
                trooplist.append(loon)
                vmap[spawnsite5[0]][spawnsite5[1]]["hover"]="y"
                vmap[spawnsite5[0]][spawnsite5[1]]["loon"]=loon.get_index()
                lcount+=1
        elif char=="6":
            if(lcount>=10):
                print("Balloon limited to 10")
            else:
                loon=troops.Balloon(100,20,2,[spawnsite6[0],spawnsite6[1]],len(loonlist))
                loonlist.append(loon)
                trooplist.append(loon)
                vmap[spawnsite6[0]][spawnsite6[1]]["hover"]="y"
                vmap[spawnsite6[0]][spawnsite6[1]]["loon"]=loon.get_index()
                lcount+=1

        elif char=="7":
            if(archcount>=10):
                print("Archers limited to 10")
            else:
                arch=troops.Archer(100,10,2,[spawnsite7[0],spawnsite7[1]],len(archlist))
                archlist.append(arch)
                trooplist.append(arch)
                vmap[spawnsite7[0]][spawnsite7[1]]["f"]="a"
                vmap[spawnsite7[0]][spawnsite7[1]]["a"]=arch.get_index()
                archcount+=1
        elif char=="8":
            if(archcount>=10):
                print("Archers limited to 10")
            else:
                arch=troops.Archer(100,10,2,[spawnsite8[0],spawnsite8[1]],len(archlist))
                archlist.append(arch)
                trooplist.append(arch)
                vmap[spawnsite8[0]][spawnsite8[1]]["f"]="a"
                vmap[spawnsite8[0]][spawnsite8[1]]["a"]=arch.get_index()
                archcount+=1
        elif char=="9":
            if(archcount>=10):
                print("Archers limited to 10")
            else:
                arch=troops.Archer(100,10,2,[spawnsite9[0],spawnsite9[1]],len(archlist))
                archlist.append(arch)
                trooplist.append(arch)
                vmap[spawnsite9[0]][spawnsite9[1]]["f"]="a"
                vmap[spawnsite9[0]][spawnsite9[1]]["a"]=arch.get_index()
                archcount+=1
        
        elif(char=="`"):
            time.sleep(0.5)

        for barb in barblist:
            speed=barb.speed
            if barb.alive==True:
                for j in range(speed):
                    barb.barb_path(villmapc,hutlist,townhall,cannonlist,walllist,wizlist)    
        for loon in loonlist:
            speed=loon.speed
            if loon.alive==True:
                for j in range(speed):
                    loon.balloon_path(villmapc,hutlist,townhall,cannonlist,wizlist)
        
        for arch in archlist:
            speed=arch.speed
            if arch.alive==True:
                for j in range(speed):
                    # print("arch ",arch.get_index())
                    # time.sleep(2)
                    arch.archer_path(villmapc,hutlist,townhall,cannonlist,walllist,wizlist)
        # checkcannons(cannonlist,villmapc,Bk)
        checkcannonsm(cannonlist,villmapc,trooplist)
        for wiztower in wizlist:
            # for j in trooplist:
            # if(wiztower.canshoot(trooplist)):
            poslist=wiztower.canshoot(trooplist)   
            if(len(poslist)==0 or poslist[0]!=-1):
                wizatlist=getwiztargets(villmapc,trooplist,poslist,barblist,loonlist,archlist)
                wiztower.shoot(wizatlist,villmapc)
                # for 
        # out=render(vmap)
        # out.draw_map()
        # time.sleep(1)
        system("clear")
        out=render(vmap)
        out.draw_map(hutlist,walllist,townhall,cannonlist,barblist,wizlist,loonlist,archlist)
        
        if(c=="k"):
            khealth=Bk.get_health()
            khealth=round(khealth,2)
        else:
            khealth=Aq.get_health()
            khealth=round(khealth,2)
        if(c=="k"):
            if(khealth>=75 and khealth<= 100):
                print("Barbarian King Health: ",khealth,"%",Fore.GREEN+"####")
                print(Style.RESET_ALL)
            elif(khealth>=30 and khealth<75):
                print("Barbarian King Health: ",khealth,"%",Fore.YELLOW+"###")
                print(Style.RESET_ALL)
            elif(khealth<30 and khealth>=10):
                print("Barbarian King Health: ",khealth,"%",Fore.RED+"##")
                print(Style.RESET_ALL)
            else:
                print("Barbarian King Health: ",khealth,"%",Fore.RED+"#")
                print(Style.RESET_ALL)
        else:
            if(khealth>=75 and khealth<= 100):
                print("Archer Queen Health: ",khealth,"%",Fore.GREEN+"####")
                print(Style.RESET_ALL)
            elif(khealth>=30 and khealth<75):
                print("Archer Queen Health: ",khealth,"%",Fore.YELLOW+"###")
                print(Style.RESET_ALL)
            elif(khealth<30 and khealth>=10):
                print("Archer Queen Health: ",khealth,"%",Fore.RED+"##")
                print(Style.RESET_ALL)
            else:
                print("Archer Queen Health: ",khealth,"%",Fore.RED+"#")
                print(Style.RESET_ALL)
        vhealth=villmapc.get_health()
        # vhealth=round(vhealth,2)
        destr=100-vhealth
        destr=round(destr,2)
        print("Destruction: ",destr,"%")
        print("Level: ",curlevel)
        time.sleep(0.5)

#function to print ascii victory art
def victory():
    print("""       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \ V /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/ """)

victory()
f.close()

    # time.sleep(1)
# print(vmap[0][0]["f"])
# print(vmap[1][0]["f"])
# print(vmap[0])