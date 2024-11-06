letters = "What are your plans for this weekend?"

# print(letters)
# print("The third letter is:", letters[2])
# print("Show everything from h all the way to the end:", letters[1:])
# print("The last stuff:", letters[-1])
# print("selective:", letters[2:4])

# print("The reversey:",letters[::-1])

#built in function examples:
print("The index for d:", letters.find('d'))

#You could build your own find
# def find(string, target):
#     index = 0
#     for char in string:
#         if char == target:
#             return index
#         index+=1
    
#     return -1 # no match

#find_all
#This function will take a string, target and return all index of the target
def find_all(string, target):
    positions = []
    index = 0
    for char in string:
        if char == target:
            positions.append(index)
        index+=1
    
    return positions

print("All matches:", find_all(letters, 'a'))

# print(letters)
# print(letters.replace("t", "yolo"))
letters = letters.replace("t", "yolo") #reassign so that the variable get updates
#letters = letters.replace("t", "yolo",1) #reassign so that the variable get updates
#use the above if you only want to change one thing not everything
print(letters)

print("hello NACA-120".capitalize())




