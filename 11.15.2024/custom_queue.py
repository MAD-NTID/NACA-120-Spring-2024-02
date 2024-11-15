queue_list = []

def empty():
    if len(queue_list) == 0:
        return True
    else:
        return False
    
    # return len(queue) == 0

def size():
    return len(queue_list)

def peek():
    if empty():
        return None
    return queue_list[0]

def enqueue(item):
    queue_list.append(item)

def dequeue():
    if empty():
        return None
    return queue_list.pop(0)
