# by Kami Bigdely
# Replace magic numbers with named constanst

COULOMB_CONSTANT = 8.9875517923*1e9


# First Section
def calculate_electirc_force():
    # Given two point charges, calcualte the electric force exerted on them.
    q1 = int(input('Enter a value of charge q1: '))
    q2 = int(input('Enter a value of charge q2: '))
    distance = int(input("Enter the distance between two charges: "))
    force = COULOMB_CONSTANT * q1 * q2/(distance**2)
    print("Electric Force between q1 and q2 is: ", force, "Newton")
    return force


# Second Section
def is_it_even_or_odd():
    # Return a string stating wither the provide number is even or odd.
    num = int(input('Enter an integer number: '))
    return (str(num) + " is an even number.") if num % 2 == 0 else (str(num) + " is an odd number.")


if __name__ == "__main__":
    # First Section
    calculate_electirc_force()
    # Second Section
    print(is_it_even_or_odd())
