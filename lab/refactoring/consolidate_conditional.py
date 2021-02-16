# by Kami Bigdely
# Consolidate conditional expressions


def dice(ingredients):
    print("diced all ingredients.")


def mix_all(diced_ingredients):
    print("mixed all.")


def add_salt():
    print('added salt.')


def pour(liquid):
    print('poured', liquid + '.',)


def make_shirazi_salad(ingredients):
    if ('cucumber' or 'tomato' or 'lemon juice' or 'onion') not in ingredients:
        print('lacks ingredients.')
        return
    diced_ingredients = dice(ingredients)
    ingreident_mix = mix_all(diced_ingredients)
    salted_mix = add_salt()
    finished_mix = pour('lemon juice')
    print('Your yummy shirazi salad is ready!')


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
