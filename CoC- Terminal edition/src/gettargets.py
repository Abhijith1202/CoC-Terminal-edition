def getbklist(Bk,villmapc,hutlist,walllist,townhall,cannlist,wizlist):
    bklist=[]
    thincl=0
    bkcoords=Bk.get_coordinates()
    left=bkcoords[1]-Bk.range
    if(left<0):
        left=0
    right=bkcoords[1]+Bk.range
    if(right>=villmapc.ubound):
        right=villmapc.ubound-1
    up=bkcoords[0]-Bk.range
    if(up<0):
        up=0
    down=bkcoords[0]+Bk.range
    if(down>=villmapc.rbound):
        down=villmapc.rbound-1
    for i in range(up,down+1):
        for j in range(left,right+1):
            if(villmapc.vmap[i][j]["f"]!="n" and villmapc.vmap[i][j]["f"]!="k"):
                temp=villmapc.vmap[i][j]["f"]
                if(temp=="h"):
                    bklist.append(hutlist[villmapc.vmap[i][j]["h"]])
                elif(temp=="w"):
                    bklist.append(walllist[villmapc.vmap[i][j]["w"]])
                elif(temp=="t"):
                    if(thincl==0):
                        bklist.append(townhall)
                        thincl=1
                elif(temp=="c"):
                    bklist.append(cannlist[villmapc.vmap[i][j]["c"]])
                elif(temp=="p"):
                    bklist.append(wizlist[villmapc.vmap[i][j]["p"]])
                # bklist.append(villmapc.vmap[i][j]["f"])
    return bklist

def getaqlist(Aq,villmapc,hutlist,walllist,townhall,cannlist,curdir,wizlist):
    aqlist=[]
    thincl=0
    aqcoords=Aq.get_coordinates()
    # left=aqcoords[1]-Aq.range
    left=aqcoords[1]-2
    if(left<0):
        left=0
    # right=aqcoords[1]+Aq.range
    right=aqcoords[1]+3
    if(right>=villmapc.ubound):
        right=villmapc.ubound-1
    # up=aqcoords[0]-Aq.range
    up=aqcoords[0]-2
    if(up<0):
        up=0
    # down=aqcoords[0]+Aq.range
    down=aqcoords[0]+3
    if(down>=villmapc.rbound):
        down=villmapc.rbound-1
    if(curdir=="w"):
        up-=8
        down-=8
        if(up<0):
            return []
    elif(curdir=="s"):
        up+=8
        down+=8
        if(down>=villmapc.rbound):
            return []
    elif(curdir=="a"):
        left-=8
        right-=8
        if(left<0):
            return []
    elif(curdir=="d"):
        left+=8
        right+=8
        if(right>=villmapc.ubound):
            return []
    for i in range(up,down+1):
        for j in range(left,right+1):
            if(villmapc.vmap[i][j]["f"]!="n" and villmapc.vmap[i][j]["f"]!="k"):
                temp=villmapc.vmap[i][j]["f"]
                if(temp=="h"):
                    aqlist.append(hutlist[villmapc.vmap[i][j]["h"]])
                elif(temp=="w"):
                    aqlist.append(walllist[villmapc.vmap[i][j]["w"]])
                elif(temp=="t"):
                    if(thincl==0):
                        aqlist.append(townhall)
                        thincl=1
                elif(temp=="c"):
                    aqlist.append(cannlist[villmapc.vmap[i][j]["c"]])
                elif(temp=="p"):
                    aqlist.append(wizlist[villmapc.vmap[i][j]["p"]])
                
    return aqlist

def getaqbiglist(Aq,villmapc,hutlist,walllist,townhall,cannlist,curdir,wizlist):
    aqlist=[]
    thincl=0
    aqcoords=Aq.get_coordinates()
    # left=aqcoords[1]-Aq.range
    left=aqcoords[1]-4
    if(left<0):
        left=0
    # right=aqcoords[1]+Aq.range
    right=aqcoords[1]+5
    if(right>=villmapc.ubound):
        right=villmapc.ubound-1
    # up=aqcoords[0]-Aq.range
    up=aqcoords[0]-4
    if(up<0):
        up=0
    # down=aqcoords[0]+Aq.range
    down=aqcoords[0]+5
    if(down>=villmapc.rbound):
        down=villmapc.rbound-1
    if(curdir=="w"):
        up-=16
        down-=16
        if(up<0):
            return []
    elif(curdir=="s"):
        up+=16
        down+=16
        if(down>=villmapc.rbound):
            return []
    elif(curdir=="a"):
        left-=16
        right-=16
        if(left<0):
            return []
    elif(curdir=="d"):
        left+=16
        right+=16
        if(right>=villmapc.ubound):
            return []
    for i in range(up,down+1):
        for j in range(left,right+1):
            if(villmapc.vmap[i][j]["f"]!="n" and villmapc.vmap[i][j]["f"]!="k"):
                temp=villmapc.vmap[i][j]["f"]
                if(temp=="h"):
                    aqlist.append(hutlist[villmapc.vmap[i][j]["h"]])
                elif(temp=="w"):
                    aqlist.append(walllist[villmapc.vmap[i][j]["w"]])
                elif(temp=="t"):
                    if(thincl==0):
                        aqlist.append(townhall)
                        thincl=1
                elif(temp=="c"):
                    aqlist.append(cannlist[villmapc.vmap[i][j]["c"]])
                elif(temp=="p"):
                    aqlist.append(wizlist[villmapc.vmap[i][j]["p"]])
                
    return aqlist

def checkcannonsm(cannonlist, villmapc, trooplist):
    for i in cannonlist:
        for j in trooplist:
            if(j.alive==False):
                continue
            coords=j.get_coordinates()
            if(villmapc.vmap[coords[0]][coords[1]]["f"]=="loon" or "hover" in villmapc.vmap[coords[0]][coords[1]]):
                if(villmapc.vmap[coords[0]][coords[1]]["hover"]=="y"):
                    continue
            if(i.canshoot(j)):
                i.toshoot(j,villmapc)
                break

def getwiztargets(villmapc,trooplist,poslist,barblist,loonlist,archlist):
    if(poslist[0]==-1):
        return []
    wizlist=[]
    up=poslist[0]-1
    if(up<0):
        up=0
    down=poslist[0]+1
    if(down>villmapc.rbound-1):
        down=villmapc.rbound-1
    left=poslist[1]-1
    if(left<0):
        left=0
    right=poslist[1]+1
    if(right>villmapc.ubound-1):
        right=villmapc.ubound-1
    for i in range(up,down+1):
        for j in range(left,right+1):
            # if(villmapc.vmap[i][j]["f"]!="n" and villmapc.vmap[i][j]["f"]!="k"):
            unit=villmapc.vmap[i][j]["f"]
            if(unit in ["k","q","b","loon","a"]):
                # wizlist.append(trooplist[villmapc.vmap[i][j]["f"]])
                if(unit=="k" or unit=="q"):
                    wizlist.append(trooplist[0])
                elif(unit=="b"):
                    index=villmapc.vmap[i][j]["b"]
                    # print(index)
                    # time.sleep(1)
                    wizlist.append(barblist[index])
                elif(unit=="a"):
                    index=villmapc.vmap[i][j]["a"]
                    wizlist.append(archlist[index])
            elif("hover" in villmapc.vmap[i][j] and villmapc.vmap[i][j]["hover"]=="y"):
                index=villmapc.vmap[i][j]["loon"]
                wizlist.append(loonlist[index])
    
    return wizlist