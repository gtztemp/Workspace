# name = input("name > ")
# print("it is good to meet you, " + name)
# print(type(name))
# age = int(input("age > "))
# print(type(age))

# for i in range(1,11):
#     print(i)

number = int(input("enter a number -> "))


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print (result, end=" ")

    return result


while number != 1:
    number = collatz(number)



