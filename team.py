import random


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # for each hero in self.heroes,
        for hero in self.heroes:
            # set the hero's current_health to their starting_health
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            hero1.fight(hero2)
            # 3) update the list of living_heroes and living_opponents
            if hero1.is_alive() == True:
                hero2.name.remove(hero2)
            # to reflect the result of the fight
            else:
                hero1.name.remove(hero1)
