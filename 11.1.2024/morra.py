
def sample_function():
    pass

"""
@author: <Your name>
date: <today's date>
Project code name: HandBattle
Purpose:
    A program that plays Morra
"""

import datetime
import random

# PREDEFINED BELOW, DO NOT MODIFY ANY CODE
LINE_SEPARATOR = "=============================="
HAND_MIN = 1
HAND_MAX = 3

"""
    This function will print the header containing 
    the game name, version number, and today's date and time
"""


def get_game_header():
    now = datetime.datetime.now()

    return \
        f"{LINE_SEPARATOR}" \
        "\nMorra" \
        "\n\tGame Version 1.0" \
        f"\n{LINE_SEPARATOR}" \
        f"\nDate and Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"


"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        game_round: The current round in the game

    returns the xp for the round
"""


def generate_xp(game_round):
    if game_round < 1:
        game_round = 1

    return random.randint(HAND_MIN, HAND_MAX) * game_round


"""
    This function will randomly pick a hand for the computer.
    This will return a hand from HAND_MIN (1) to HAND_MAX (3)
"""


def get_computer_hand():
    return random.randint(HAND_MIN, HAND_MAX)


"""
    This function will return a random hand sum guess for the computer.
    This will return a hand sum from HAND_MIN * 2 + HAND_MIN * 2
"""


def get_computer_guess():
    return random.randint(HAND_MIN, HAND_MAX) + random.randint(HAND_MIN, HAND_MAX)
# PREDEFINED ABOVE, DO NOT MODIFY ANY CODE


# STUDENT CODE HERE
def determine_winner(player_hand, player_guess, computer_hand, computer_guess):
    both_hand_sum = player_hand + computer_hand

    if player_guess == both_hand_sum:
        return "player"
    elif computer_guess == both_hand_sum:
        return "computer"
    elif player_guess == both_hand_sum and computer_guess == both_hand_sum:
        return "tie"
    else:
        return "no winner"

def get_player_hand():
    while True:
        try:
            player_hand = int(input(f"Play a hand between {HAND_MIN} and {HAND_MAX}: "))

            if player_hand >= HAND_MIN and player_hand <= HAND_MAX:
                return player_hand
            
            print(f"Invalid Hand Range, must be between {HAND_MIN} and {HAND_MAX}")
        except ValueError:
            print("Invalid Input")
        print()

def get_player_guess():
    while True:
        try:
            user_guess = int(input(f"Guess the sum of both hands between {HAND_MIN * 2} and {HAND_MAX * 2}: "))

            if user_guess >= HAND_MIN * 2 and user_guess <= HAND_MAX * 2:
                return user_guess
            
            print(f"Invalid Guess, must be between {HAND_MIN * 2} and {HAND_MAX * 2}")
        except ValueError:
            print("Invalid Input")
        print()

def get_stats(player_score, player_wins, computer_score, computer_wins):
    player_statistics = "================================="
    player_statistics += f"\n   Player Score: {player_score}"
    player_statistics += f"\n    Player Wins: {player_wins}"
    player_statistics += f"\n Computer Score: {computer_score}"
    player_statistics += f"\n  Computer Wins: {computer_wins}"

    return player_statistics

    # return \
    #     f"==============================" \
    #     f"\n   Player Score: {player_score}" \
    #     f"\n    Player Wins: {player_wins}" \
    #     f"\n Computer Score: {computer_score}" \
    #     f"\n  Computer Wins: {computer_wins}"

def get_play_again_prompt():
    while True:
        response = input("Do you want to play again (yes or quit): ").lower()

        if response == "yes" or response == "quit":
            return response
        else:
            print("Invalid Response\n")

def main():
    player_score = 0
    player_wins = 0
    computer_score = 0
    computer_wins = 0
    game_round = 1

    # STUDENT CODE HERE
    print(get_game_header())

    while True:
        if game_round > 1:
            print(get_stats(player_score, player_wins, computer_score, computer_wins))

        print(f"Round: {game_round}")

        # Get Computers Hand and Guess, and Store to Variables (do not print it)
        computer_hand = get_computer_hand()
        computer_guess = get_computer_guess()

        player_hand = get_player_hand()
        player_guess = get_player_guess()

        print(f"Computer's Hand: {computer_hand}")
        print(f"Computer's Guess: {computer_guess}")

        print(f"The Sum of both hands is {computer_hand + player_hand}\n")

        winner = determine_winner(player_hand, player_guess, computer_hand, computer_guess)

        if winner == "player":
            print("Player won the round!")
            player_score += generate_xp(game_round)
            player_wins += 1
        elif winner == "computer":
            print("Computer won the round")
            computer_score += generate_xp(game_round)
            computer_wins += 1
        elif winner == "tie":
            print("It's a tie")
        else:
            print("No Winner")

        prompt_response = get_play_again_prompt()

        if prompt_response == "yes":
            game_round += 1
        else:
            break

    print("Thank you for playing Morra!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was ended abruptly by the user\n")
