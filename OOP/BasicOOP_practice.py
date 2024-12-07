# Create a class “Programmer” for storing information of few programmers working at Microsoft. 
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 1200000, 400092)
print(p.name, p.company, p.salary, p.pin)
r = Programmer("Sammy", 120202, 600098)
print(r.name, r.company, r.salary, r.pin)

# Write a class “Calculator” capable of finding square, cube and square root of a number. Also add a static method to greet the user
# with hello

class Calculator:
    def __init__(self, n):
        self.n = n

    def sqaure(self):
        print(f"The sqaure is {self.n * self.n} ")
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n} ")
    def sqaureRoot(self):
        print(f"The sqaureRoot is {self.n ** 1/2} ")

    @staticmethod
    def greeting():
        print("Hello there!")

c = Calculator(4)
c.greeting()
c.sqaure()
c.cube()
c.sqaureRoot()

#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. 
# Does this change the class attribute?   ANS :- NO

class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute. It has NOT changed

# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)  and get fare information of train running.
from random import randint
class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self,fro, to):
        print(f"The ticket is booked in train number {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train number {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"The ticket fare for train number {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

VandeBharat = Train(22224)
VandeBharat.book("Dadar", "Nashik")
VandeBharat.getStatus()
VandeBharat.getFare("Dadar", "Nashik")


    