# You can use while loop for counting but it's not preferable
times_to_loop = 10
current_loop = 1

while current_loop <= times_to_loop:
    print(f"Currently at {current_loop}")
    # current_loop += 1 # increment by one, otherwise you'll never break out
    # you'll be in a loop prison forever...

print("Done looping")


for current_loop in range(times_to_loop):
    print(f"Currently at {current_loop}")