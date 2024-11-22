def sum_of_number_loop(n):
    num = 0
    
    for y in range(1, n + 1):
        num += y

    return num


def sum_of_number_recursion(n):
    # base case
    if n == 1:
        return 1

    return n + sum_of_number_recursion(n-1)


# print(sum_of_number_loop(10))
print(sum_of_number_recursion(10))
