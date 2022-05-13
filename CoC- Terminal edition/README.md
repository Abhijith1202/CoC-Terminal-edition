# Clash Of Clans Ultra Lite

## Introduction
A basic replica of Clash of Clans, with a few tweaks. This is a lightweight version of Clash of Clans that is designed to be used on a Linux device (May or may not work on Windows, as I have tested it only on windows)

## How to start playing
After extracting, just use `python3 game.py` to start the game.
A prompt will appear asking you to choose a hero: k for barbarian king or q for archer queen

## Controls:
- Basic `wasd` controls the Barbarian King's movements (who is shown as the Blue "k")
- Press < Spacebar > to use the Barbarian king's Axe or archer queen's crossbow, which does area damage to a range of 2 tiles from the king or an area from the queen's position
- Press `1`, `2`or `3` to spawn a barbarian in corresponding spawn point (no cheating. Only 10 barbarians allowed xP)
- Press `4`, `5`or `6` to spawn a balloon in corresponding spawn point (no cheating. Only 10 barbarians allowed xP)
- Press `7`, `8`or `9` to spawn a archer in corresponding spawn point (no cheating. Only 10 barbarians allowed xP)
- Press `r` to activate rage spell
- Press `h` to activate heal spell
- Press `x` for the op range attack of the archer queen (if youve selected her ofcourse)
- Press `q` to quit the game

## Troops:
- Barbarian King:
    - HP: 2000
    - Attack: 50
    - Speed: 1
    - Range: 2
    - Attack Type: area damage

- Archer Queen:
    - HP: 1000
    - Attack: 30
    - Speed: 1
    - Range: 8 tiles from the queen
    - Attack Type: area damage (5x5)
    - Special attack: 16 tiles from queen, 9x9 area damage

- Barbarian:
    - HP: 100
    - Attack: 10
    - Speed: 1
    - Range: 1
    - Attack Type: Single target

-  Archer
    - HP: 100
    - Attack: 10  
    - Speed: 2
    - Range: 5
    - Attack Type: Single target

- Balloon:
    - HP: 100
    - Attack: 20
    - Speed: 2
    - Range: 1
    - Attack Type: Single target


## Buildings:
- Townhall:
    - HP: 300
    - Dimensions: 4x3

- Hut:
    - HP: 100
    - Dimensions: 1x1

- Cannons:
    - HP: 60
    - Dimensions: 1x1
    - Damage per shot: 20
    - Attack Type: Single target
    - Speed: 1
    - Range: 6

- Walls:
    - HP: 200
    - Dimensions: 1x1

- Wizard tower:
    - HP: 80
    - Dimensions: 1x1
    - Damage: 10
    - Attack Type: AoE
    - Speed: 1
    - AoE: 3x3
    - Range: 6

## Spells:
- Rage:
    - Effect: All troops' attack and speed is increased by 100%
    - Key: R
- Heal:
    - Effect: All alive troops' HP is increased to 150% of their current HP (capped at 100%)
    - Key: H

## Criteria for the game to end:
### Victory!
- You win the game if you destroy all the buildings that are not walls (with at least one troop remaining, of course), across all three levels

### Defeat:
- You lose the game if all of your troops die without getting 100% destruction.

## Replay:
- All the attacks done are stored in the `replays` folder
- The filenames are in the form `mm:dd:HH:MM:SS.txt`
- To simulate the replay of an attack, say `sunny.txt`, use `python3 replay.py replays/sunny.txt`