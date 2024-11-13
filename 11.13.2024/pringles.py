import stack


def create_new_pringles(chip_count):
    # Fill the tube with the given count of chips
    for i in range(chip_count):
        stack.push(f"Chip {i + 1}")


def main():
    # prompt for if user wants to add chip to the tube?
    # assume data is valid (positive integer, no float)
    chip_count = int(input("How many chips do you want in the Pringles tube? "))
    create_new_pringles(chip_count)

    while not stack.empty():
        remaining_chips = stack.size()
        print(f"You have {remaining_chips} Pringle chips left to eat")
        print()

        # prompt the user how many chips they want to eat? (assume data is positive integer)
        chips_to_eat = int(input("How many chips do you want to eat? "))
        if stack.size() >= chips_to_eat:
            for i in range(chips_to_eat):
                # eat a chip, print before eating (the top obviously, unless you cheat like Nai)
                chip_to_eat = stack.pop()
                print(f"You ate {chip_to_eat}")
        else: 
            print(f"Sorry, you can't eat more chips than available {stack.size()} in the Pringles tube")
            continue

    print(f"You ate the whole entire Pringles tube. Now be a buddy and recycle that tube!")  


main()
