# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("Saved into Databse")


if __name__ == "__main__":
    inputed_username = input('Please enter your username: ')
    save_into_db(inputed_username)

    inputed_year = int(input('Please enter your birth year: '))
    age = 2020 - inputed_year
    print("You are", age, "years old.")
