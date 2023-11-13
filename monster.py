
from copy import *
from random import randint

monsterlist = []
class monster:
    def __init__(self, name = str, hprangemin = int, hprangemax = int):
        self.name = name
        self.hprangemin = hprangemin
        self.hprangemax = hprangemax
        self.maxhp = randint(self.hprangemin, self.hprangemax)
        self.hp = self.maxhp
        self.block = 0
        monsterlist.append(self)

    def create(self):
        return monster(self.name, self.hprangemin, self.hprangemax)


goblin = monster("Goblin", 14, 22)
ghoul = monster("Ghoul", 5, 12)

def randcreate(list = []):
    choice = list[randint(0, len(list) -1)]
    creation = choice.create()
    return creation

enemy1 = randcreate(monsterlist)
enemy2 = randcreate(monsterlist)

print(enemy1.name, enemy1.hp, enemy1.maxhp)
print(enemy2.name, enemy2.hp, enemy2.maxhp)


