class Prey:

    def flee(self):
        print("This animal flees")

class Predators:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predators):
    pass

class Fish(Prey, Predators):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
#hawk.hunt()
#fish.flee()
#fish.hunt()
