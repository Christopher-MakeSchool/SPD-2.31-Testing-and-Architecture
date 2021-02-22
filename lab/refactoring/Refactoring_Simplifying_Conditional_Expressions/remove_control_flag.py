# by Kami Bigdely
# Remove control flag


def find_food(food, fridge):
    for item in fridge:
        if item is food:
            return True
    return False


if __name__ == "__main__":
    food = 'wesabi'
    food_list = ['onion', 'cucumber', 'Guacamole', 'kabob barg', 'wesabi']
    found_item = find_food(food, food_list)
    print("Looking for", food, "\nDid we find it?\t " + str(found_item))
