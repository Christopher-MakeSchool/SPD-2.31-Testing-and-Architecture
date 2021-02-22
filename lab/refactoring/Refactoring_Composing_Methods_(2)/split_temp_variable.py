# by Kami Bigdely
# Split temporary variable

patty = 70  # [gr]
pickle = 20  # [gr]
tomatoes = 25  # [gr]
lettuce = 15  # [gr]
buns = 95  # [gr]
kimchi = 30  # [gr]
mayo = 5  # [gr]
golden_fried_onion = 20  # [gr]


ny_burger_weight = (2 * patty + 4 * pickle + 3 *
                   tomatoes + 2 * lettuce + 2 * buns)

kimchi_burger_weight = (2 * patty + 4 * pickle + 3 * tomatoes +
                   kimchi + mayo + golden_fried_onion + 2 * buns)


if __name__ == "__main__":
    print(f"NY Burger Weight {ny_burger_weight}lbs")
    print(f"Seoul Kimchi Burger Weight {kimchi_burger_weight}lbs")
