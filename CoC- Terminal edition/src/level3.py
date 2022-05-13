from input import *
from colorama import Fore, Back, Style
import troops
import buildings
from village import villagemap
from render import render
from gettargets import *

import time
import spell
import datetime


def getl3map():
    vmap = [[{"f": "n"} for i in range(100)] for j in range(35)]
    villmapc = villagemap(vmap, 0, 35, 0, 100, 0, 0, 0)
    townhall = buildings.Townhall(300, [10, 10], "t")
    villmapc.curbuild += 1
    villmapc.curbuildhp += townhall.basehitpoints
    villmapc.basehp += townhall.basehitpoints
    for i in range(3):
        for j in range(4):
            vmap[10-i][10+j]["f"] = "t"
    hutlist = []
    cannonlist = []
    walllist = []
    hut1 = buildings.Hut(100, [5, 5], "h")
    hut2 = buildings.Hut(100, [5, 15], "h")
    hut3 = buildings.Hut(100, [15, 5], "h")
    hut4 = buildings.Hut(100, [15, 15], "h")
    hut5 = buildings.Hut(100, [10, 25], "h")
    villmapc.curbuild += 5
    villmapc.curbuildhp += hut1.basehitpoints+hut2.basehitpoints + \
        hut3.basehitpoints+hut4.basehitpoints+hut5.basehitpoints
    villmapc.basehp += hut1.basehitpoints+hut2.basehitpoints + \
        hut3.basehitpoints+hut4.basehitpoints+hut5.basehitpoints
    hutlist.append(hut1)
    hutlist.append(hut2)
    hutlist.append(hut3)
    hutlist.append(hut4)
    hutlist.append(hut5)
    for i in range(5):
        coords = hutlist[i].get_coordinates()
        # print(coords)
        # print(coords[0])
        vmap[coords[0]][coords[1]]["f"] = "h"
        vmap[coords[0]][coords[1]]["h"] = i
        # print(vmap[coords[0]])

    offsetl = 3
    # offsetr=17
    offsetd = 3
    numwalls = 0
    # offsetu=27
    for i in range(14):
        if(i == 0 or i == 13):
            for j in range(24):
                wall = buildings.Wall(200, [i+offsetl, j+offsetd], "w")
                walllist.append(wall)
                vmap[i+offsetl][j+offsetd]["f"] = "w"
                vmap[i+offsetl][j+offsetd]["w"] = numwalls
                numwalls += 1
                # villmapc.curbuild+=1
        else:
            wall = buildings.Wall(200, [i+offsetl, offsetd], "w")
            walllist.append(wall)
            vmap[i+offsetl][offsetd]["f"] = "w"
            vmap[i+offsetl][offsetd]["w"] = numwalls
            numwalls += 1
            wall = buildings.Wall(200, [i+offsetl, offsetd+23], "w")
            walllist.append(wall)
            vmap[i+offsetl][offsetd+23]["f"] = "w"
            vmap[i+offsetl][offsetd+23]["w"] = numwalls
            numwalls += 1


    c1 = buildings.Cannon(60, [7, 20], 20, "c")
    c2 = buildings.Cannon(60, [13, 20], 20, "c")
    c3 = buildings.Cannon(60, [10, 5], 20, "c")
    c4=buildings.Cannon(60, [7, 5], 20, "c")
    villmapc.curbuild += 4
    villmapc.curbuildhp += 4*c1.basehitpoints
    villmapc.basehp += 4*c1.basehitpoints
    cannonlist.append(c1)
    cannonlist.append(c2)
    cannonlist.append(c3)
    cannonlist.append(c4)
    vmap[7][20]["f"] = "c"
    vmap[7][20]["c"] = 0
    vmap[13][20]["f"] = "c"
    vmap[13][20]["c"] = 1
    vmap[10][5]["f"] = "c"
    vmap[10][5]["c"] = 2
    vmap[7][5]["f"] = "c"
    vmap[7][5]["c"] = 3

    w1 = buildings.Wizardtower(80, [10, 20], 10, "p")
    villmapc.curbuild += 1
    villmapc.curbuildhp += w1.basehitpoints
    villmapc.basehp += w1.basehitpoints
    wizlist = [w1]
    vmap[10][20]["f"] = "p"
    vmap[10][20]["p"] = 0

    w2 = buildings.Wizardtower(80, [5, 10], 10, "p")
    villmapc.curbuild += 1
    villmapc.curbuildhp += w2.basehitpoints
    villmapc.basehp += w2.basehitpoints
    vmap[5][10]["f"] = "p"
    vmap[5][10]["p"] = 1

    w3 = buildings.Wizardtower(80, [15, 10], 10, "p")
    villmapc.curbuild += 1
    villmapc.curbuildhp += w3.basehitpoints
    villmapc.basehp += w3.basehitpoints
    vmap[15][10]["f"] = "p"
    vmap[15][10]["p"] = 2

    w4=buildings.Wizardtower(80, [12, 5], 10, "p")
    villmapc.curbuild += 1
    villmapc.curbuildhp += w4.basehitpoints
    villmapc.basehp += w4.basehitpoints
    vmap[12][5]["f"] = "p"
    vmap[12][5]["p"] = 3

    wizlist.append(w2)
    wizlist.append(w3)
    wizlist.append(w4)

    return villmapc, vmap, hutlist, cannonlist, walllist, wizlist, townhall
