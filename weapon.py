import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        # //2 is a force integer function
        weapon_value = random.randint(self.max_damage//2, self.max_damage)
        return weapon_value
