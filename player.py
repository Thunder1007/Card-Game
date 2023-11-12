

from card import *

class player:
    def __init__(self, name, maxhp) -> None:
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.block = 0
        self.deck = []
        self.str = int
        self.dex = int
        
thunder = player("Thunder", 40)

