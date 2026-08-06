while True:
    try:
        number = int(input("Enter a number -> "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        print("Input is not valid !!!")


print(number, end=" ")


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result, end=" ")

    return result


while number != 1:
    number = collatz(number)

# Another way
# def get_number():
#     while True:
#         try:
#             number = int(input("Enter a number -> "))
#             if number > 0:
#                 return number
#             print("Enter a positive number!")
#         except ValueError:
#             print("Input is not valid !!!")


# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     return 3 * number + 1


# number = get_number()

# while number != 1:
#     print(number, end=" ")
#     number = collatz(number)

# print(1)
