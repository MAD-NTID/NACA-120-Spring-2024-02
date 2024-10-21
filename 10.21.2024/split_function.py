# Type a sentence, it can be anything... this sentence will be used to perform a word search
sentence = input("Enter a sentence: ")
print(f"Old Sentence: {sentence}")

# We need 'sanitize' the sentence so as to remove symbols that may interfere with a word search when splitting
# Remember, splitting by a given delimeters will break the string in to a list of words. And you can use this 
# list of words to perform a word search, but they may contain characters like 'hello,...!' and then your search
# won't work.

# The very long and boring way to sanitize a sentence
# sentence_without_symbols = sentence.replace(",", "")
# sentence_without_symbols = sentence_without_symbols.replace(".", "")
# sentence_without_symbols = sentence_without_symbols.replace("!", "")

# The shorter way to sanitize a sentence, supposed you want to remove over 100 symbols (this is the way to go)
sentence_without_symbols = sentence
for symbol in ".,!":
    sentence_without_symbols = sentence_without_symbols.replace(symbol, "")

# Print out the new santized sentence
print(f"New Sentence: {sentence_without_symbols}")

# Prompt the user what word to search for in the sentence
search_for = input("Enter a word to search: ")

# Finally, split the new sanitized sentence by the space delimiter " "
# This will give you a list of words
split_sentence = sentence_without_symbols.split(" ")

# Use for loop to find the word
for word in split_sentence:
    # we force lower case each comparison to ensure is case 'insensitive' meaning, something like this could work
    # 'HELLO' == 'heLLo' because .lower() will make it so that 'hello' == 'hello'
    if search_for.lower() == word.lower():
        print(f"Word was found '{search_for}'")