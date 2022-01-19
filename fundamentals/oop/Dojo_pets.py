class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.feed()
        return self
    def bathe(self):
        self.pet.bathe()
        return self

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def play(self):
        self.health += 5
        print("I'm playing")
        return self
    def feed(self):
        print("I'm feed")
        return self
    def bathe(self):
        print("I'm clean")
        return self
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def noise(self):
        print('bark! bark!')
Caesar = Pet('Caesar', 'Husky', 'roll over', 70, 70)

Tom = Ninja('Tom', 'Thompson', Caesar, 'bone', 'tuna')
Tom.feed()
Tom.walk()
Tom.bathe()