def sum(num1, num2):
    # at the moment, it is concatenating two strings into one
    result = num1 + num2
    return result

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# Different ways of displaying data
print("The result is " + str(sum(num1, num2)))
print("The result is", sum(num1, num2))
print(f"The result is {sum(num1, num2)}")
print("The result is {sum}".format(sum=sum(num1, num2)))
