# A list of magics
magics = ['unicorn', 'rainbow', 'stuff2', 'stuff3']
#prompt the user for the magic to search for in the magics list
magic_target = input("Enter your magic target:")
if magic_target in magics: #if the magic is in the list,we found a match
    print("We found the magic")
else:#otherwise the magic is not in the lsit
    print("No such magic was found")
print()


#Loop forever

while True:
    #prompt for sentence
    sentence = input("Enter some string:")
    #prompt for target to search for
    target = input("What do you want to search for:")

    
    found=False
    #words = sentence.split(' ') #make each word in a list of words
    # for word in words:
    #     if word == target:
    #         found=True
    #         break

    #use in to make the above code simplier
    if target in sentence:
        found = True

    if found:
        print("A match was found!")
    else:
        print("No match was found")