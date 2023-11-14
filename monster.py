
from player import *
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
    
    def attack(self, amount):

        if player.block > 0:
            if amount <= player.block:
                player.block -= amount

            else:
                player.block = 0
                amount -= player.block
                player.hp -= amount

    def getblock(self, amount):
        self.block += amount


def randcreate(list = []):
    choice = list[randint(0, len(list) -1)]
    creation = choice.create()
    return creation


goblin = monster("Goblin", 14, 22)
ghoul = monster("Ghoul", 5, 12)


enemy1 = randcreate(monsterlist)
enemy2 = randcreate(monsterlist)

print(enemy1.name, enemy1.hp, enemy1.maxhp)
print(enemy2.name, enemy2.hp, enemy2.maxhp)


