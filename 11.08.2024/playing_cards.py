import random

# a function to use to shuffle the cards
def shuffle(cards):
    #for i from n−1 down to 1 do
    n = len(cards)
    for i in range(n-1,0,-1):
        #j ← random integer such that 0 ≤ j ≤ i
        j = random.randrange(0,i+1)

        #exchange a[j] and a[i]
        #store the old value of j before swap
        temp = cards[j]
        cards[j] = cards[i]
        cards[i] = temp


# a list to store all cards
cards = []

# each cards will have those suits
suits = ("Diamond", "Heart", "Spade", "Club")

#create the ranks. we have from 2-10, then J,Q,K,A. We will agree that 11 is J, 12 is Q etc
for num in range(2,15):
    if num == 11:
        rank = "Jack"
    elif num == 12:
        rank = "Queen"
    elif num == 13:
        rank = "King"
    elif num == 14:
        rank = "Ace"
    else:
        rank = str(num)
    
    #we will create 4 suits for each ranks
    for suit in suits:
        #we made the assumption that the color is red
        color = "Red"
        #however if the suit happens to be club or spade then we change to black
        if suit in ["Club", "Spade"]:
            color = "Black"
        
        #create a tuple representation of the card
        card = (rank, suit, color)

        #add to the list of cards
        cards.append(card)


print("Here are the cards")
#print(cards)
print(f"There are {len(cards)} cards")
for card in cards:
    print(card)

print("Suffling the cards")
shuffle(cards)
for card in cards:
    print(card)


