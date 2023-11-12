
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
                    print(f"{self.list.count(x)}x {str(x)}")

strike = card("Strike", 1, "Deal 6 damage")
defend = card("Defend", 1, "Gain 5 Block")

drawpile = cardlist("Draw Pile", [strike, strike, defend, defend])
hand = cardlist("Hand", [strike, strike, strike])
discardpile = cardlist("Discard Pile", [defend, strike, defend])
deck = cardlist("Deck", [])

drawpile.showcards()
hand.showcards()
discardpile.showcards()
deck.showcards()
