from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # instance variables named team_one and team_two hold teams.
        self.team_one = list()
        self.team_two = list()

    def create_ability(self):
        # prompts for the info to make an ability + max_damage
        name = input("What is the ability name?")
        max_damage = input("What is the max damage of the ability?")
        return Ability(name, max_damage)

    def create_weapon(self):
        # prompts for the info to make a weapon + max_damage
        name = input("What is the weapon name?")
        max_damage = input("What is the max damage of the weapon?")
        return Weapon(name, max_damage)

    def create_armor(self):
        # prompts for the info to make add armor + max_block
        name = input("What is the armor name?")
        max_block = input("What is the max the armor blocks?")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # add an ability to the hero
                self.create_ability()
                hero.add_ability(self.create_ability)
            elif add_item == "2":
                # add a weapon to the hero
                self.create_weapon()
                hero.add_ability(self.create_weapon)
            elif add_item == "3":
                # add an armor to the hero
                self.create_armor()
                hero.add_ability(self.create_armor)
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(
            input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            # call self.create_hero() for every hero that the user wants to add to team one.
            hero = self.create_hero()
            # Add the created hero to team one.
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(
            input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            # call self.create_hero() for every hero that the user wants to add to team one.
            hero = self.create_hero()
            # Add the created hero to team one.
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        print(f'-----{self.team_one.name} STATS------')
        self.team_one.show_stats()
        print(f'-----{self.team_two.name} STATS------')
        self.team_two.show_stats()
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:

        # for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #

        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #

        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
