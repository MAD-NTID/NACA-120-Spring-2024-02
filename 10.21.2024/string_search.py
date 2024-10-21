word_search = input("Enter a word to search: ")
built_string = ""

for character in "Hello World, this is my favorite world!":
    # Reset building the string if a blank character is hit
    if character == " ":
        built_string = ""
        continue #  Skip the current iteration and continue to the next
    
    built_string = built_string + character

    # Compare if the words match so far
    if word_search.lower() == built_string.lower():
        print(f"Found word '{word_search}'")