# by Kami Bigdely
# Inline method.

LEGAL_DRINKING_AGE = 21


class Person:
    def __init__(self, my_age):
        self.age = my_age


def enter_night_club(individual):
    print("Allowed to enter.") if individual.age > LEGAL_DRINKING_AGE else print(
        "Entrance of minors is denied.")


if __name__ == "__main__":
    person = Person(17.9)
    enter_night_club(person)
