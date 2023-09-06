'''
************************************************************************************************

Simple python engine that renders a basic Dongeons and Dragons character alla character sheet,
but hopefully cutting some edges regarding decision making while creating a character, as well
as making some variables randmomizable.

All of the game's variables, as well as naming conventions have been extracted from the 
Basic Rules' hanbook, published in November 2018 and available for free in the official game's 
website.

*************************************************************************************************
'''
import random
from time import sleep

# Steps to build a character
# 1. choose a race

RACES = [
    "Mountain dwarf", 
    "Hill dwarf", 
    "High elf",
    "Wood elf",
    "Lightfoot hafling", 
    "Stout halfling", 
    "Human"]
    
alignments = [
    ("Lawful good", 9),
    ("Neutral good", 8),
    ("Chaotic good", 7),
    ("Lawful neutral", 6),
    ("Neutral", 5),
    ("Chaotic neutral", 4),
    ("Lawful evil", 3),
    ("Neutral evil", 2),
    ("Chaotic evil", 1)
]

class Dice():
    def __init__(self, size):
        if not size:
            raise ValueError("Missing number of die's size")
        self.size = size
    
    def rollDice(self):
        return random.randint(1, self.size)

    def printDie(int):
        print("rolling dice...")
        sleep(3.5)
        print()
        print("\t", end="")

        print(int)

class MountainDwarf():
    def __init__(self):
        self.speed = 7.5 #speed in meters
        self.heigth = 120.0
        self.youngestYearsOfAge = 15.0
        self.oldestYearsOfAge = 350.0

        self.alignment = 0 # initialized to zero but redifined by random


class Elf():
    def __init__(self):
        self.speed = 9.1
        self.heigth = (152 + 183) / 2 
        self.youngestYearsOfAge = 15.0
        self.oldestYearsOfAge = 750.0
        self.alignment = 0

class Randomize():
    def __init__(self, clss):
        if not clss:
            raise ValueError("Missing class")
        self.clss = clss

    def randomizeAge(self):
        #returns random age of the dwarf    
        return random.randint(self.clss.youngestYearsOfAge, self.clss.oldestYearsOfAge) 


    def randomizeHeight(self):
        # two rolls of a 4 size die 
        roll_dice = Dice(4)
        firstRoll = roll_dice. rollDice() * 2.5
        secondRoll = roll_dice.rollDice() * 2.5

        return firstRoll + secondRoll + self.clss.heigth
    
    def randomizeAlignment(self):
        rollDice = Dice(8) #dice[n - 1]
        randNum = rollDice.rollDice()
        return randNum 

def main():
    my_elf = Elf()
    create_elf = Randomize(my_elf)
    print(create_elf.randomizeHeight())
    print(create_elf.randomizeAge())
    alignment = create_elf.randomizeAlignment()

    print(alignments[alignment][0])


# def main():
    
#     print('''Welcome to the D&D character generator!
# You can choose between 4 races, which have been paired with two of their sub-races
# for the sake of convenience (except humans, which have no sub-race). 
# That make a total of {} available races. These are:'''.format(len(RACES)))
#     print()

#     for race in range(len(RACES)):
#         print(RACES[race])
#     print()

#     print("Generating character...")
#     sleep(3)
#     print()

#     print("Character race: {}".format(RACES[0]))
#     my_dworf = MountainDwarf()
#     print("Generated heigth: {} cm".format(my_dworf.randomizeHeight()))
#     print()

#     print("Generated age: {}".format(my_dworf.randomizeAge()))
#     print()

#     alignment = my_dworf.randomizeAlignment()
#     print("Generated alignment: {}".format(alignments[alignment][0]))
#     #assign the random number to the class
#     my_dworf.alignment = alignments[alignment][1]

if __name__== "__main__":
     main()

