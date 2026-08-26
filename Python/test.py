# Ex-1
# name = 'Gaurav'
# message = 'would you like to learn python?'
# print (f'Hello {name}, {message}')
# output= Hello Gaurav, would you like to learn python?

# Ex-1.1
# author = 'Albert Einstein'
# quote = 'A person who never made a mistake never tried anything new.'
# print (f'{author} once said, "{quote}"')
# output = Albert Einstein once said, "A person who never made a mistake never tried anything new."

# Ex-2
# n = int(input("Number - "))
# for i in range (1, n+1):
#     print(" "* (n-i),"*"* (2*i-1))

# Ex-2.1
# rows = int(input("Number - "))
# for i in range(rows):
#     spaces = ' ' * (rows - i - 1)
#     stars = '*' * (2 * i + 1)
#     print(spaces + stars)

# Ex-3.1
# class Employee:
#     language = "python"
#     salary = 120
#     def getInfo(self):
#             print(f"The language is {self.language} and the salary is {self.salary}") #will be called as harry.language harry.salary

# harry = Employee()
# harry.language = "Java" #will override python
# Employee.getInfo(harry) #or# harry.getInfo()

# Ex-3.2
# class Employee:
#     language = "python"
#     salary = 120

# def getInfo(emp):
#     print(f"The language is {emp.language} and the salary is {emp.salary}")

# harry = Employee()
# getInfo(harry)  # Pass the object manually


# name = input("name > ")
# print("it is good to meet you, " + name)
# print(type(name))
# age = int(input("age > "))
# print(type(age))

# for i in range(1,11):
#     print(i)

print("hello")