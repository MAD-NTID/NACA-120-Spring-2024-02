prompt = "Do you want to play again(yes/no)? "
response = True # Default

while(response):
    print("Game is playing... weeeee yoohoo, you die")

    response = input(prompt)

    if response.lower() == 'yes':
        response = True
    else:
        response = False

print("Game Over! You suck!")