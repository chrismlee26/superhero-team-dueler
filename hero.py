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
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        # Hasn't been tested yet
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        # We're here right now
        for ability in self.abilities:
            total_damage -= ability.defend()
            return total_block

    def take_damage(self):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        self.opponent = opponent
        duel = [opponent.name, self.name]
        print("The winner is: ", random.choice(duel))

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
if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
