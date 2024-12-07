# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))

# average = (a + b + c) / 3
# print(average)

# Making a basic function
def func1():
    print("hello bhai")

func1()

# Practice
# FUNCTION DEFINITION
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    avg = (a + b + c) / 3
    print(avg)

avg() #FUNCTION CALL

#Function with arguments

def greet(name, ending):
    print("Good day, " + name)
    print(ending)
    return "ok"
a = greet("Samarth", "Thank you bhai")
print(a)

# Default paramter value
def goodDay(name, ending="Thank you"):
    print(f"Hello, {name}")
    print(ending)

goodDay("Samarth") #OUTPUT :- Hello, Samarth /n Thank you
goodDay("Sammy", "thanksss")

# Code to find the factorial of a number
def factorial(n):
    if(n == 0 or n ==1):
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is {factorial(n)}")



