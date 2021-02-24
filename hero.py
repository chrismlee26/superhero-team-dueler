import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.kills = 0
        self.deaths = 0

    def add_kill(self, sum_kills):
        # update self kills by num_kills amount
        self.kills += sum_kills

    def add_death(self, sum_deaths):
        # update self deaths by num_deaths amount
        self.deaths += sum_deaths

    def add_weapon(self, weapon):
        # adds a weapon into the abilities list object
        self.abilities.append(weapon)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, def_damage):
        total_def = 0
        for armor in self.armors:
            if self.armors == 0:
                print('no armor')
            else:
                total_def += armor.block()
        return def_damage - total_def

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        return self.current_health

    def is_alive(self):
        if self.current_health >= 0:
            return True
        else:
            return False

    def fight(self, opponent):
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # create variables to hold abilities.length
        hero_abilities = len(self.abilities)
        hero2_abilities = len(opponent.abilities)
        # force int on abilties lists and check if greater than zero
        if int(hero_abilities) <= 0 or int(hero2_abilities) <= 0:
            print("Draw")
        # 1) else, start the fighting loop until a hero has won
        else:
            # loop as long as heros are not dead
            while self.current_health > 0 and opponent.current_health > 0:
                # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
                # 3) After each attack, check if either the hero (self) or the opponent is alive
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
                # if hero1 is alive then print
                if self.is_alive() == True:
                    print(f'${self.name} won!')
                    self.add_kill += 1
                    opponent.add_death += 1

                else:
                    # if opponent is alive then print
                    print(f'${opponent.name} won!')
                    opponent.add_kill += 1
                    self.add_death += 1

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
# if __name__ == "__main__":
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health, 'how much hp left')
    # hero.take_damage(150)
    # print(hero.is_alive(), '-------------isalive------------')
    # hero.take_damage(15000)
    # print(hero.is_alive(), '-------------isdead------------')


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

# Test for add_weapons first integration
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     hero = Hero("Wonder Woman")
#     weapon = Weapon("Lasso of Truth", 90)
#     hero.add_weapon(weapon)
#     print(hero.attack())
