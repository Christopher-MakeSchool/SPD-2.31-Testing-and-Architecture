# by Kami Bigdely
# Extract Class


class Food:
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingridients, recipe):
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingridients = ingridients
        self.recipe = recipe

    def description(self):
        print("Name:", self.name)
        print("Prep time:", self.prep_time, "mins")
        print("Is Veggie?", 'Yes' if self.is_veggie else "No")
        print("Food Type:", self.food_type)
        print("Cuisine:", self.cuisine)
        print("Ingridients: ", end='')
        for item in self.ingridients:
            print(item, end=', ')
        print("Recipe:")
        for step in self.recipe:
            print("Step:", step)
        print("***")

butternut_squash_soup = Food(name='butternut squash soup',
                             prep_time=45,
                             is_veggie=True,
                             food_type='soup',
                             cuisine='North African',
                             ingridients=['butter squash', 'onion', 'carrot', 'garlic',
                                          'butter', 'black pepper', 'cinnamon', 'coconut milk'],
                             recipe=['1. Grill the butter squash, onion, carrot and garlic in the oven until they get soft and golden on top',
                                     '2. Put all in blender with butter and coconut milk. Blend them till they become puree.',
                                     '3. Then move the contents into a pot and Add coconut milk. Simmer for 5 mintues.'])

shirazi_salad = Food(name='shirazi salad',
                     prep_time=5,
                     is_veggie=True,
                     food_type='salad',
                     cuisine='Iranian',
                     ingridients=['cucumber', 'tomato', 'onion', 'lemon juice'],
                     recipe=['1. dice cucumbers, tomatoes and onions',
                             '2. put all into a bowl',
                             '3. pour lemon juice add salt',
                             '4. Mixed them thoroughly'])

home_made_beef_sausage = Food(name='Home-made Beef Sausage',
                              prep_time=60, 
                              is_veggie=False,
                              food_type='deli',
                              cuisine='All',
                              ingridients=['sausage casing', 'regular ground beef', 'garlic',
                                           'corriander seeds', 'black pepper seeds', 'fennel seed', 'paprika'],
                              recipe=['1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make the seasonings.',
                                      '2. In a bowl, mix ground beef with the seasoning.',
                                      '3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel.',
                                      '4. Rotate the stuffer\'s handle (or turn it on) to make your yummy sausages!'])

butternut_squash_soup.description()
shirazi_salad.description()
home_made_beef_sausage.description()
