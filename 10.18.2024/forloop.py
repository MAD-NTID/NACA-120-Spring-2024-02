# for loop
# loops until a specific amount of times given is reached
# is a pre-test loop (checks for conditions before looping)

# loop 5 times
# the i is the current int of the iteration without starting point therefore, starts with 0
for i in range(5):
    print(f"This is the {i} loop")

print()

# what if we don't want it to print 0 but 1 to 5 instead
for i in range(1, 6):
    print(f"This is the {i} loop")

print()

for i in range(5):
    print(f"This is the {i + 1} loop")

print()

# You can also specify a stepping number, skip a number after each print
for i in range(1, 21, 2):
    print(f"This is the {i} loop")

print()

# Let's do loops by collecting user input
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
step = int(input("Enter the stepping value: "))

for i in range(start, end, step):
    print(f"This is the {i} loop")
