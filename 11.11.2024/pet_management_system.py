# Dictionary for Records
pet_records = {}

def menu():
    menu = [
        "Add a New Pet (name, age, type, patient number)",
        "Remove a Pet by (patient number)",
        "List All Pet",
        "List A Pet by (patient number)",
        "List All Data",
        "Exit",
    ]

    # Show the User the Options, and select a "valid" option
    while True:
        print("\nMenu")
        for option in range(len(menu)):
            print(f"{option + 1}. {menu[option]}")

        selection = input("Select an Option: ")
        if not selection.isdigit():
            print("Invalid Selection")
            continue

        selection = int(selection)
        if selection < 1 or selection > len(menu):
            print(f"Invalid Selection, pick between 1 and {len(menu)}")
            continue

        return selection

# Option 1
def add_new_pet(type, name, age, patient_number):
    new_pet = {
        'type': type,
        'name': name, 
        'age': age,
        'patient_number': patient_number
    }

    # Add this New Pet to the Pet Records
    pet_records[patient_number] = new_pet

# Option 2
def remove_a_pet(patient_number):
    if patient_number in pet_records:
        return pet_records.pop(patient_number)

    return False

# Option 3
def list_all_pet():
    if len(pet_records) > 0:
        print("All Pets: ")

        for pet in pet_records:
            this_pet = pet_records[pet]
            print(f"Patient Number: {this_pet['patient_number']}, Type: {this_pet['type']}, Name: {this_pet['name']}, Age: {this_pet['age']}")
    else:
        print("No Pet Records to Show")


# Option 4
def list_a_pet(patient_number):
    if patient_number in pet_records:
        return pet_records[patient_number]

    return False


# Option 5
def list_all_data():
    if len(pet_records) > 0:
        for key, value in pet_records.items():
            print(f"Key: {key}, Value: {value}")
    else:
        print("No Pet Records to Show")


def main():
    while True:
        selection = menu()

        if selection == 1:
            while True:
                type = input("Enter the Type of Pet: ")

                if type == "" or type is None:
                    print("Type is Required")
                else:
                    break
            
            while True:
                name = input("Enter the name of the Pet: ")

                if name == "" or name is None:
                    print("Name is Required")
                else:
                    break
            
            
            while True:
                age = input("Enter the Age of the Pet: ")

                if not age.isdigit() and int(age) < 0:
                    print("Invalid Age")
                else:
                    break
            
            while True:
                patient_number = input("Enter the Patient Number of the Pet: ")

                if not patient_number in pet_records:
                    add_new_pet(type, name, age, patient_number)
                    break
                else:
                    print(f"Patient Number {patient_number} is already used")
                    continue

            print(f"A New Pet Record was added: \nDetails - {pet_records[patient_number]}")
        elif selection == 2:
            patient_number = input("Enter the Patient Number of the Pet to Remove: ")

            # if the pet was found and poppped, it wll return a dictionary of the pet
            # otherwise, it will return a bool (False)
            show_a_pet = remove_a_pet(patient_number)

            # if the variable removed_pet has 'something', it's a True by default
            # otherwise, it's not True (False)
            if show_a_pet:
                print(f"Pet {show_a_pet} was removed")
            else:
                print(f"Pet with patient number {patient_number} was not found")
        elif selection == 3:
            list_all_pet()
        elif selection == 4:
            patient_number = input("Enter the Patient Number of the Pet to Show: ")
            
            show_a_pet = list_a_pet(patient_number)

            # if the variable show_a_pet has 'something', it's a True by default
            # otherwise, it's not True (False)
            if show_a_pet:
                print(f"Pet: {show_a_pet}")
            else:
                print(f"Pet with patient number {patient_number} was not found")
        elif selection == 5:
            list_all_data()
        elif selection == 6:
            break
        else:
            print("No idea what happened here...")

        # Add a Space for each Loop
        print()


    print("Thank you for using our famous Pet Management System")
    print("Bye bye")

main()