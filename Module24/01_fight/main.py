import random

class Warrior:

    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def round_info(self):
        print(self.name, '=', self.HP)

npc_1 = Warrior("Воин_1", 100)
npc_2 = Warrior("Воин_2", 100)
warrior_list = [npc_1,npc_2]
while True:
    who = random.choice(warrior_list)
    if npc_1.HP == 0:
        print("Winner = ", npc_2.name)
        break
    elif npc_2.HP == 0:
        print("Winner = ", npc_1.name)
        break
    print("Beat = ", who.name)
    if who.name != npc_1.name:
            npc_1.HP -= 20
            npc_1.round_info()
    elif who.name != npc_2.name:
            npc_2.HP -= 20
            npc_2.round_info()







