# The elements for the stack, an empty list
elements = []

# Gets whether the list is empty or not
def empty():
    # if len(elements) == 0:
    #     return True
    # else:
    #     return False
    
    if len(elements) == 0:
        return True
    return False

    # return len(elements) == 0

# Gets the size of the list
def size():
    return len(elements)

# Retrieves the top element of the list
def peek():
    if not empty():
        return elements[0]
    return None

# Adds a new element to the top of the list
def push(element):
    elements.insert(0, element)

# Retrieves the top element, and then remove it from the list
def pop():
    if not empty():
        return elements.pop(0)
    return None