words = ["hello", "world", "this", "is", "a", "list", "of", "words"]

def single_word_search(target, index=0):
    # base case 1
    if index < 0 or index >= len(words):
        return None
    
    # case insensitive and base case 2
    if words[index].lower() == target.lower():
        return words[index]
    
    # return is not needed here, but added for clarity
    return single_word_search(target, index + 1)


# run program (prompt the user only if __name__ is in fact ran as file like 'python .\word_search.py')
if __name__ == "main":
    target = input("Enter a word to search: ")

    if single_word_search(target):
        print(f"Word found: {target}")
    else:
        print(f"Word {target} not found")