

from random import randint

class monster:
    def __init__(self, name = str, hprangemin = int, hprangemax = int):
        self.name = name
        self.hprangemin = hprangemin
        self.hprangemax = hprangemax
        self.maxHP = randint(hprangemin, hprangemax)
        self.hp = self.maxHP
        self.block = 0
        
goblin = monster("Goblin", 14, 22)

print(goblin.maxHP)