

from cardeffect import *
class card:
    def __init__(self, name, basemana, effect):
        
        self.name = name
        self.basemana = basemana
        self.mana = basemana
        self.effect = effect
        
    def __str__(self) -> str:
        return f"{self.name} ({self.basemana} Mana): {self.effect}."


class cardlist:
    def __init__(self, name, list = []):
        self.name = name
        self.list = list
        self.size = len(self.list)
        
    def showcards(self):
    
        dupecheck = []
        if len(self.list) == 0:
            print(f"Your {self.name} is empty!")
        else:
            print(f"Your {self.name} contains the following cards:")
            for x in self.list:
                if x in dupecheck:
                    continue
            
                else:
                    dupecheck.append(x)
                    print(f"{str(x)} (x{self.list.count(x)})")


    def choosecard(self):

        indexdict = {}
        index = 0

        if len(self.list) == 0:
            print(f"There are no cards in your {self.name} to choose from!")
            return 0
        else:
            indexdict[0] = 0
            for x in self.list:
                if x in indexdict.values():
                    continue
            
                else:

                    index += 1
                    indexdict[index] = x

        for x, y in indexdict.items():
            if x == 0:
                if self == hand:
                    print(f"[{x}]: None -> End Turn!")
                else:
                    print(f"[{x}]: None -> Return!")
            
            else:
                print(f"[{x}]: {y} (x{self.list.count(y)})")
                     
        while True:

            choice = input("\nType the index of the card you want to choose: ")

            try:
                choice = int(choice)
            except ValueError:
                print(f"{choice} is not a number! Please enter a valid number! ")
                continue
            
            if choice in indexdict.keys():
                break
            else:
                print(f"{choice} is not a valid number! Please enter the number of the card you want to choose!")
                continue

        return indexdict[choice]


strike = card("Strike", 1, "Deal 6 damage")
defend = card("Defend", 1, "Gain 5 Block")
slam = card("SLAM!", 3, "Deal 22 damage")
defensive_jab = card("Defensive Jab", 1, "Deal 3 damage and gain 3 block")
pocket_sand = card("Pocket Sand", 0, "Deal 2 damage")


drawpile = cardlist("Draw Pile", [strike, strike, defend, defend])
hand = cardlist("Hand", [strike, strike, strike])
discardpile = cardlist("Discard Pile", [defend, strike, defend])
deck = cardlist("Deck", [])

