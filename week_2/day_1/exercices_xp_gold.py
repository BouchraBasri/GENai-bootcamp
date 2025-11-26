# Exercice 1
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def definition(self):
        print("A circle is a shape consisting of all points in a plane that are at a fixed distance (radius) from a center point.")

# Exercice 2
import random

class MyList:
    def __init__(self):
        self.mylist = []

    def reversed_list(sekf, original_list):
        reversed_list = []
        temp = original_list[:]   # Copy to avoid destroying the original
        while temp:
            reversed_list.append(temp.pop())
        return reversed_list

    def sorted_list(self, original_list):
        return sorted(original_list)


    def second_list(self):
        length = len(self.mylist)
        second_list = []
        
        for n in range(length):
            second_list.append(random.randint(0, 100))
        
        return second_list

ml = MyList()

print("=== TEST 1: reversed_list ===")
original = [1, 2, 3, 4]
print("Original:", original)
print("Reversed:", ml.reversed_list(original))


print("\n=== TEST 2: sorted_list ===")
unsorted_list = [4, 1, 3, 2]
print("Original:", unsorted_list)
print("Sorted:", ml.sorted_list(unsorted_list))


print("\n=== TEST 3: second_list ===")
ml.mylist = [10, 20, 30]   
print("ml.mylist =", ml.mylist)
print("second_list (random numbers):", ml.second_list())
