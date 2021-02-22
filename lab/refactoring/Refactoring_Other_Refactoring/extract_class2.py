# by Kami Bigdely
# Extract class

class Person():
    def __init__(self, first_name, last_name, birth_year, email=None, movies=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
        self.movies = movies

    def add_email(self, email_address):
        self.email = email_address

    def moves_played(self, movies):
        self.moveis.append(movies)


def send_hiring_email(email):
    print("email sent to: ", email)


if __name__ == "__main__":
    elizabeth_debicki = Person('Elizabeth', 'debicki', 1990, 'deb@makeschool.com', 
                               ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'])
    jim_carrey = Person('Jim', 'Carrey', 1962, 'jim@makeschool.com',
                        ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'])
    people = [elizabeth_debicki, jim_carrey]

    for person in people:
        if person.birth_year > 1985:
            print(person.first_name, person.last_name)
            print('Movies Played: ', end='')
            for m in person.movies:
                print(m, end=', ')
            print()
            send_hiring_email(person.email)