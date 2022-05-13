from textwrap import indent
from colorama import Fore, Back, Style
from village import villagemap

class render:
    def __init__(self,vmap):
        self.vmap=vmap
    
    def draw_map(self,hutlist,walllist,townhall,cannlist,barblist,wizlist,loonlist,archlist):
        for i in self.vmap:
            for j in i:
                if j["f"]=="n":
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                            print(Back.GREEN+" ",end="")
                    else:
                        print(Back.GREEN+" ",end="")
                elif j["f"]=="k":
                    print(Back.BLUE+"K",end="")
                elif j["f"]=="q":
                    print(Back.LIGHTBLUE_EX+"Q",end="")
                elif j["f"]=="b":
                    index=j["b"]
                    health=barblist[index].get_health()
                    if(health>=50):
                        print(Back.YELLOW+"B",end="")
                    else:
                        print(Back.RED+"B",end="")
                elif j["f"]=="a":
                    index=j["a"]
                    health=archlist[index].get_health()
                    if(health>=50):
                        print(Back.LIGHTMAGENTA_EX+"R",end="")
                    else:
                        print(Back.MAGENTA+"R",end="")

                elif j["f"]=="t":
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                        # index=j["t"]
                            health=townhall.get_hp()
                            if(health>=70 and health<=100):
                                print(Back.YELLOW+"T",end="")
                            elif(health>=30 and health<70):
                                print(Back.WHITE+"T",end="")
                            else:
                                print(Back.RED+"T",end="")
                    else:
                    # index=j["t"]
                        health=townhall.get_hp()
                        if(health>=70 and health<=100):
                            print(Back.YELLOW+"T",end="")
                        elif(health>=30 and health<70):
                            print(Back.WHITE+"T",end="")
                        else:
                            print(Back.RED+"T",end="")

                elif j["f"]=="h":
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                            index=j["h"]
                            health=hutlist[index].get_hp()
                            if(health>=70 and health<=100):
                                print(Back.BLACK+"H",end="")
                            elif(health>=30 and health<70):
                                print(Back.YELLOW+"H",end="")
                            else:
                                print(Back.RED+"H",end="")
                    else:
                        index=j["h"]
                        health=hutlist[index].get_hp()
                        if(health>=70 and health<=100):
                            print(Back.BLACK+"H",end="")
                        elif(health>=30 and health<70):
                            print(Back.YELLOW+"H",end="")
                        else:
                            print(Back.RED+"H",end="")

                elif j["f"]=="w":
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                            index=j["w"]
                            health=walllist[index].get_hp()
                            if(health>=50):
                                print(Back.RED+"W",end="")
                            else:
                                print(Back.LIGHTRED_EX+"W",end="")
                    else:
                        index=j["w"]
                        health=walllist[index].get_hp()
                        if(health>=50):
                            print(Back.RED+"W",end="")
                        else:
                            print(Back.LIGHTRED_EX+"W",end="")

                elif j["f"]=="c":
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                            index=j["c"]
                            health=cannlist[index].get_hp()
                            flashing=cannlist[index].get_flashing()
                            if(health>=70 and health<=100):
                                # print(Back.WHITE+"C",end="")
                                if(flashing):
                                    print(Back.CYAN+"C",end="")
                                else:
                                    print(Back.WHITE+"C",end="")
                            elif(health>=30 and health<70):
                                if(flashing):
                                    print(Back.CYAN+"C",end="")
                                else:
                                    print(Back.BLACK+"C",end="")
                            else:
                                
                                if(flashing):
                                    print(Back.CYAN+"C",end="")
                                else:
                                    print(Back.RED+"C",end="")
                    else:
                        index=j["c"]
                        health=cannlist[index].get_hp()
                        flashing=cannlist[index].get_flashing()
                        if(health>=70 and health<=100):
                            # print(Back.WHITE+"C",end="")
                            if(flashing):
                                print(Back.CYAN+"C",end="")
                            else:
                                print(Back.WHITE+"C",end="")
                        elif(health>=30 and health<70):
                            if(flashing):
                                print(Back.CYAN+"C",end="")
                            else:
                                print(Back.BLACK+"C",end="")
                        else:
                            
                            if(flashing):
                                print(Back.CYAN+"C",end="")
                            else:
                                print(Back.RED+"C",end="")

                elif j["f"]=="p": #wizard tower
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                            index=j["p"]
                            health=wizlist[index].get_hp()
                            flashing=wizlist[index].get_flashing()
                            if(health>=70):
                                if(flashing):
                                    print(Back.LIGHTMAGENTA_EX+"P",end="")
                                else:
                                    print(Back.CYAN+"P",end="")
                            elif(health>=30 and health <70):
                                if(flashing):
                                    print(Back.LIGHTMAGENTA_EX+"P",end="")
                                else:
                                    print(Back.LIGHTBLUE_EX+"P",end="")
                            else:
                                if(flashing):
                                    print(Back.LIGHTMAGENTA_EX+"P",end="")
                                else:
                                    print(Back.RED+"P",end="")
                    else:
                        index=j["p"]
                        health=wizlist[index].get_hp()
                        flashing=wizlist[index].get_flashing()
                        if(health>=70):
                            if(flashing):
                                print(Back.LIGHTMAGENTA_EX+"P",end="")
                            else:
                                print(Back.CYAN+"P",end="")
                        elif(health>=30 and health <70):
                            if(flashing):
                                print(Back.LIGHTMAGENTA_EX+"P",end="")
                            else:
                                print(Back.LIGHTBLUE_EX+"P",end="")
                        else:
                            if(flashing):
                                print(Back.LIGHTMAGENTA_EX+"P",end="")
                            else:
                                print(Back.RED+"P",end="")

                else:
                    if("hover" in j):
                        if(j["hover"]=="y"):
                            index=j["loon"]
                            health=loonlist[index].get_health()
                            if(health>=50):
                                print(Back.RED+"L",end="")
                            else:
                                print(Back.LIGHTRED_EX+"L",end="")
                        else:
                            print(Back.GREEN+" ",end="")
                    else:
                        print(Back.GREEN+" ",end="")
                # if("hover" in j):
                #     if(j["hover"]=="y"):
                #         print(Back.LIGHTRED_EX+"B",end="")
            print(Style.RESET_ALL)
            # print()get_
        print(Style.RESET_ALL)