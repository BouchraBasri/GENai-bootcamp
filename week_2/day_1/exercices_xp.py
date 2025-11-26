# Exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name  = cat_name
        self.age = cat_age

cat1 = Cat("Mimi", 4)
cat2 = Cat("Luna", 7)
cat3 = Cat("Simba", 2)

def find_oldest_cat(cat1, cat2, cat3):
    return max([cat1, cat2, cat3], key=lambda cat: cat.age)

oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

# Exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

ahmeds_dog = Dog("Rex", 50)
saras_dog = Dog("Teacup", 20)

print(f"Ahmad's dog is {ahmeds_dog.name}, height: {ahmeds_dog.height} cm")
ahmeds_dog.bark()
ahmeds_dog.jump()

print(f"Sara's dog is {saras_dog.name}, height: {saras_dog.height} cm")
saras_dog.bark()
saras_dog.jump()

if ahmeds_dog.height > saras_dog.height:
    print(f"The bigger dog is {ahmeds_dog.name}.")
else:
    print(f"The bigger dog is {saras_dog.height}.")

# Exercice 3
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print("".join(self.lyrics))

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

# Exercice 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        groups = {}

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        self.animals.sort()
        group = {}

        for animal in self.animals:
            letter = animal[0].upper()
            if letter not in group:
                group[letter] = [animal]
            else:
                group[letter].append(animal)
        
        self.groups = group
        return group
    
    def get_groups(self):
        print(self.groups)

casa_zoo = Zoo("Casa Zoo")

casa_zoo.add_animal("cat")
casa_zoo.add_animal("dog")
casa_zoo.get_animals()
casa_zoo.sell_animal("dog")
casa_zoo.get_animals()
casa_zoo.add_animal("cow")
casa_zoo.add_animal("lion")
casa_zoo.add_animal("monkey", "donkey", "tiger")
casa_zoo.get_animals()
casa_zoo.sort_animals()
casa_zoo.get_groups()

