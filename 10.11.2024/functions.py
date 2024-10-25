def say_hello_world():
    print("Hello World")


def box():
    print(
    """
    ==============================
    ||                          || 
    ||                          || 
    ||                          || 
    ||                          || 
    ==============================
    """)


def greet_this_person(name):
    print("Hello there, your name is " + name)


def get_your_favorite_number():
    number = input("Enter your favorite number: ")
    return number


def power(base, power):
    result = 1
    for n in range(power): #range means between 1 up to whatever value in power
        result = result * base

    return result


def main():
    # say_hello_world()
    # box()

    # print("Your favorite number is " + get_your_favorite_number())

    # name = input("What is your name? ")
    # greet_this_person(name)

    print("The result for 2 to the power of 4 is", power(2, 4))


main()