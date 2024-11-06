#The actual pin number
PIN= 5555

while True:
    #prompt for pin number
    pin = input("Enter the pin number:")
    #ensure that the pin numbers are digits
    if pin.isdigit()!=True:
        print("Numbers only!")
        continue
    if len(pin)!=4:#ensure that there are 4 digits
        print("Pin numbers must be 4 digits!")
        continue

    #convert to int and compare against the actual pin
    if int(pin)==PIN:
        print("Welcome... here is 1 million dollars")
        break

    print("Invalid pin number!")