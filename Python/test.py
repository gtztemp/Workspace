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
        print(number // 2)
    else:
        print(3 * number + 1)

    return 

collatz(number)



