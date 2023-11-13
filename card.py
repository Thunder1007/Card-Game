
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

    def getindexdict(self):

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

        print(indexdict)
        return indexdict

    def showindexdict(self):
        for x in 
        
    #wie willst du das machen??? get, show, beides???
            


strike = card("Strike", 1, "Deal 6 damage")
defend = card("Defend", 1, "Gain 5 Block")

drawpile = cardlist("Draw Pile", [strike, strike, defend, defend])
hand = cardlist("Hand", [strike, strike, strike])
discardpile = cardlist("Discard Pile", [defend, strike, defend])
deck = cardlist("Deck", [])

discardpile.getindexdict()