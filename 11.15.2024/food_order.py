import custom_queue

print("Yarin is hungry, and goes to DC to Order Cheeseburger")
custom_queue.enqueue("Yarin")
print("Yarin got in line")
print()

print("Who's in the front? Should be Yarin")
print(custom_queue.peek())
print()

print("Nai Nai and Bat are tossing a quarter for head and tails, on who goes first. Bat wins")
custom_queue.enqueue("Bat")
print("Bat got in the line")
print()

print("Who's in the front? Should be Yarin")
print(custom_queue.peek())
print()

print(f"How many people in line? {custom_queue.size()}")
print()

print(f"{custom_queue.dequeue()} got his order and went to chomp it up")
print()

print("Who's in the front? Should be Bat")
print(custom_queue.peek())
print()