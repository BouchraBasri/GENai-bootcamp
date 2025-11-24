# Exercice 1
car_model = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

car_model_list = car_model.split(",")

print(f"There are {len(car_model_list)} companies in the list.")

print("Manufacteurers in the list in descending order (Z-A): ")
print(sorted(car_model_list, reverse=True))

count_o = 0
for car in car_model_list:
    if 'o' in car.lower():
        count_o += 1 

print(f"There are {count_o} manufacturers have the letter 'o' in them.")

count_i = 0
for car in car_model_list:
    if 'i' not in car.lower():
        count_i +=1

print(f"There are {count_i} manufacturers don't have the letter 'i' in them.")

manufacturers = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

manufacturers = set(manufacturers)
print(', '.join(manufacturers))
print(f"There are {len(manufacturers)} conmpanies in the list.")

reversed_names = [car[::-1] for car in manufacturers]
print("manufacturers A-Z but reversed letters: ")
print(reversed_names)