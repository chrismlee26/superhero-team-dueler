import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, armor=0):
        total_def = 0
        # print(total_def, self.current_health, "total_def + current health L28")
        # print(type(total_def))
        if self.current_health <= 0:
            # print(type(total_def), "total_def typeof L31")
            return total_def
        else:
            # print("armor list", self.armors)
            for armor in self.armors:
                total_def = armor.block()  # block comes from from armor.py class
                # print(armor.block(), "armor")
                return total_def

    def take_damage(self, damage):
        # print(self.defend(), "-----take damage---")
        self.current_health -= damage - self.defend(damage)
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        # self.opponent = opponent
        # duel = [opponent.name, self.name]
        # print("The winner is: ", random.choice(duel))

        # ----------- TESTING / PRINT STATEMENTS BELOW --------------------
        # Fight Test
        # if __name__ == "__main__":
        #     hero1 = Hero("Wonder Woman")
        #     hero2 = Hero("Dumbledore")
        #     hero1.fight(hero2)
        # Override default current_health Test
        # if __name__ == "__main__":
        #     my_hero = Hero("Grace Hopper", 200)
        #     print(my_hero.name)
        #     print(my_hero.current_health)
        # Add ability to list test
        # if __name__ == "__main__":
        #     ability = Ability("Great Debugging", 50)
        #     hero = Hero("Grace Hopper", 200)
        #     hero.add_ability(ability)
        #     print(hero.abilities)
        # Attack Test for abilities
        # if __name__ == "__main__":
        #     ability = Ability("Great Debugging", 50)
        #     another_ability = Ability("Smarty Pants", 90)
        #     hero = Hero("Grace Hopper", 200)
        #     hero.add_ability(ability)
        #     hero.add_ability(another_ability)
        #     print(hero.attack())

        # Test Take Damage + alive/dead
if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health, 'how much hp left')
    hero.take_damage(150)
    print(hero.is_alive(), '-------------isalive------------')
    hero.take_damage(15000)
    print(hero.is_alive(), '-------------isdead------------')
