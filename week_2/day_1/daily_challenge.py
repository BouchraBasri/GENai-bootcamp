class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}
    
    def add_animal(self, **kwargs):
        for animal, count in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += count
            else:
                self.animals[animal] = count
            
            print(f"{animal} added successfully.")


    def get_info(self):
        print(f"{self.farm_name}'s farm\n")
        print("The animals:\n") 
        for animal, count in self.animals.items():
            print(f"{animal}: {count}")
        print("E-I-E-I-O!")
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_list = self.get_animal_types()
        animal_str = []
        for animal in animal_list:
            count = self.animals[animal]

            if count > 1:
                animal_str.append(animal + "s")
            else:
                animal_str.append(animal)

        if len(animal_str) == 1:
            animal_string = animal_str[0]
        else:
            animal_string = ", ".join(animal_str[:-1]) + " and " + animal_str[-1]
            
        return f"{self.farm_name}'s farm has {animal_string}"    
        
            

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)

macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
macdonald.get_info()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())