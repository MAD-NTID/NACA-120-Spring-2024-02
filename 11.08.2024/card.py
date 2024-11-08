"""
    A tuple representation of a card.
    A card is made up of :
        - rank
        - suit
        - color
"""
card = ("Jack", "Diamond", "Black")
#alternative way of creating a tuple
#card = tuple(("Jack", "Diamond", "Black"))
print(card)
print(type(card))
print("Total number of elements in the card:", len(card))
print("The rank of the card is:", card[0])

print("Is the word 'Black' in the card?", "Black" in card)

print("Attempt to change the rank of the card")
card[0] = "Ace"