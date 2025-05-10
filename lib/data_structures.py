spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
# problem 1
def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods ]
    return names
    
print(get_names(spicy_foods))

# problem 2
def get_spiciest_foods(spicy_foods):
    spice = [food for food in spicy_foods if (food["heat_level"] > 5)]
    return spice

print(get_spiciest_foods(spicy_foods))

# problem 3
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spice_level = "🌶" * food["heat_level"]
        food = food["name"] + " (" + food["cuisine"] + ") | Heat Level: " +spice_level
        print(food)

print_spicy_foods(spicy_foods)

# problem 4
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

print(get_spicy_food_by_cuisine(spicy_foods, "American"))

# problem 5
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] >5:
            spice_level = "🌶" * food["heat_level"]
            food = food["name"] + " (" + food["cuisine"] + ") | Heat Level: " +spice_level
            print(food)

print_spiciest_foods(spicy_foods)

#problem 6
def get_average_heat_level(spicy_foods):
    heat = []
    for food in spicy_foods:
        heat.append(food["heat_level"])
    average = sum(heat) / len(spicy_foods)
    return average

print(get_average_heat_level(spicy_foods))

# problem 7
def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods


print(create_spicy_food(spicy_foods, {"name": input("Food name: "), "cuisine": input("Cuisine: "), "heat_level": int(input("Heat Level: "))}))
