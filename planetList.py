planet_list = ["Mercury", "Mars"]

# 1. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# append adds one item to the list
planet_list.append("Jupiter")
planet_list.append("Saturn")

# 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# extend adds more than one item to the list
planet_list.extend(["Uranus", "Neptune"])

# 3. Use insert() to add Earth, and Venus in the correct order.
# insert an item at a given position
print(planet_list)
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")


