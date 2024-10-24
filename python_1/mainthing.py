# Descriptive variable names
favorite_food = "cake"
least_favorite_food = "spinach"

# Function to check food preference
def check_food_preference(food):
    """Checks if the given food is the user's favorite or least favorite."""
    if food == favorite_food:
        print(f"My favorite food is {food}.")
    elif food == least_favorite_food:
        print(f"My least favorite food is {food}.")
    else:
        print(f"I don't have any strong feelings about {food}.")

# Testing the function with different foods
check_food_preference("cake")
check_food_preference("spinach")
check_food_preference("apple")

# Use different data types
age = 25  # integer
rating = 4.5  # float
foods = ["cake", "spinach", "apple"]  # list

# Loop through the list to show repeated tasks
print("\nFood preferences:")
for food in foods:
    check_food_preference(food)

# Dictionary example
food_ratings = {
    "cake": 5,
    "spinach": 2,
    "apple": 4
}

# Display food ratings
print("\nFood ratings:")
for food, rating in food_ratings.items():
    print(f"{food}: {rating}/5")

# Demonstrating variable reassignment with different data types
x = 4  # integer
print(x)
x = "Hello there"  # string
print(x)
x = 3.14  # float
print(x)
