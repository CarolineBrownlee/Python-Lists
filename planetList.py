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
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

# 4. Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")

# 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
# slice by creating a new list cutting off at proper index
rocky_planets = planet_list[:4]
print(rocky_planets)

# 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
# remove() works the same as del operation, example below
# planet_list.remove("Pluto")
del planet_list[8]
print(planet_list)






