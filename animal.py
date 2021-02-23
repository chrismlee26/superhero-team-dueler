class Animal:
    def __init__(self, name, sleep_time):
        self.name = name
        self.sleep_time = sleep_time

    def sleep(self):
        print("{} sleeps for {} hours".format(self.name, self.sleep_time))


class Dog(Animal):
    def bark(self):
        print('woof!')


my_dog = Dog("bob", 18)
my_dog.sleep()
my_dog.bark()
