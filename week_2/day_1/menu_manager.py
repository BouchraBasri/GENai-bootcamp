# Exercice 3 (Exercice xp gold)
class MenuManager:
    def __init__(self):
        self.menu = [
             {"name": "Soup", "price": 10, "spice_level": "B", "gluten_index": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten_index": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten_index": False},
            {"name": "French Fries", "price": 5,  "spice_level": "C", "gluten_index": False},
            {"name": "Beef Bourguignon", "price": 25, "spice_level": "B", "gluten_index": True},
        ]

    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name": name,
            "price": price,
            "spice_level": spice,
            "gluten_index": gluten
        }

        self.menu.append(new_dish)
        print(f"{name} was added to the manu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice_level"] = spice
                dish["gluten_index"] = gluten
                print(f"{name} was updated successfully!")
                return
        print(f"{name} is not in the menu. Cannot be updated!")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name.lower():
                self.menu.remove(dish)
                print(f"{name} is removed")
                print("Updated list: ", self.menu)
                return
        
        print(f"{name} is not in the menu. Cannot be removed.")

if __name__ == "__main__":
    manager = MenuManager()

    print("Initial menu:")
    print(manager.menu)

    print("\n--- Adding Pizza ---")
    manager.add_item("Pizza", 20, "A", True)
    print(manager.menu)

    print("\n--- Updating Soup ---")
    manager.update_item("Soup", 12, "C", True)
    print(manager.menu)

    print("\n--- Trying to update something not in menu ---")
    manager.update_item("Ice Cream", 5, "A", False)

    print("\n--- Removing Salad ---")
    manager.remove_item("Salad")

    print("\n--- Trying to remove something not in menu ---")
    manager.remove_item("Chocolate Cake")
