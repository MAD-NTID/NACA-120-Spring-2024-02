import re

# Predefined variables
games_records = [] #this will keep a list of all game sales

# Predefined function
def display_menu():
    print("Menu Options:")
    print("1. Create a new sale")
    print("2. Remove a record")
    print("3. Show all sales")
    print("4. Filter sale by platform")
    print("5. Exit")
    
# Predefined function
def menu_selection():
    display_menu()
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            
            return choice
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# functions to be completed by the student goes here
def is_valid_date(date_str):
    # if the pattern match is not None, then it's a match and therefore true
    pattern = r'\d{2}-\d{2}-\d{4}'
    return re.search(pattern, date_str) is not None

    # return bool(re.fullmatch(pattern, date_str))

def create_sale():
    # name of the game, game platform, date-of-sale, cost-of-the-game
    name = input("Enter the name of the game: ")
    platform = input("Enter the platform of the game: ")

    while True:
        date = input("Enter a Date of Sale (MM-DD-YYYY): ")
        if is_valid_date(date):
            break

        print("Invalid date of sale. Ensure it is in MM-DD-YYYY format")

    cost = float(input("Enter the cost of the game: "))

    # Create a Sales Record Dict
    game_record = {
        "name": name,
        "platform": platform,
        "date": date,
        "cost": cost
    }

    # Finally, add to the list of games
    games_records.append(game_record)

def remove_record():
    if not games_records:
        print("No games to show")
        return

    game_name = input("Enter the name of the game to remove: ")
    platform = input("Enter the platform for the game to remove: ")

    for game in games_records:
        if game["name"].lower() == game_name.lower() and game["platform"].lower() == platform.lower():
            games_records.remove(game)
            return True
        
    return False

def show_sales():
    if len(games_records) == 0:
        print("The list is currently empty")
    else:
        print(games_records)

def filter_by_platform_rec(record_list, target, filtered_list):
    # base
    if len(record_list) == 0:
        return filtered_list
    
    # we compare the item at index 0
    game_record = record_list[0]
    if game_record["platform"].lower() == target.lower():
        filtered_list.append(game_record)

    # now, we will shorten the record_list ignoring the recent game at index 0
    # so let's make a copy starting at index 1 and onward
    # the long way below
    # 
    # copy_record_list = []
    # for i in range(1, len(record_list) - 1):
    #     copy_record_list.append(record_list[i])
    # 
    # Then do recursion
    # return filter_by_platform_rec(copy_record_list, target, filtered_list)

    # or shortcut (best way) 
    record_list = record_list[1:]
    return filter_by_platform_rec(record_list, target, filtered_list)

def filter_by_platform():
    platform = input("Enter the platform to filter games: ")

    filtered_list = filter_by_platform_rec(games_records, platform, [])

    if len(filtered_list) == 0:
        print(f"No games were found matching the platform '{platform}'")
    else:
        print(filtered_list)

def main():
    while True:
        try:
            selected_menu = menu_selection()

            if selected_menu == 1:
                create_sale()

            elif selected_menu == 2:
                if remove_record():
                    print("Game record removed successfully")
                else:
                    print("Could not find that game record to remove")
            
            elif selected_menu == 3:
                show_sales()

            elif selected_menu == 4:
                filter_by_platform()

            else:
                print("Thank you for using Electronic Arts (EA) gaming store. Good Bye")
                break
            
            # Adds an empty space between each iteration for readability
            print()
        except:
            print("Invalid Action!")
    

if __name__ == "__main__":
    main()