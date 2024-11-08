#create list to hold the cards
cards = [] 



#create two different cards using a tuple
card1 = ("Jack", "Diamond", "Black")
card2 = ("Ace", "Heart", "Red")

#add the cards to the list
cards.append(card1)
cards.append(card2)


#show all cards
print(cards)

print(f"There are {len(cards)} card(s)")

print("The first card is:", cards[0])
card1 = cards[0]
print("The rank of the first card is:", card1[0])