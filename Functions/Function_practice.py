# Write a program using functions to find greatest of three numbers. 
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 23
b = 28
c = 11
print(greatest(a, b, c))

# Write a python program using function to convert Celsius to Fahrenheit. 
# c/5 = (f-32)/9   c= 5*(f-32)/9
# without function:-
'''f = float(input("Enter temperature in F: "))
c= 5*(f-32)/9
print(c)'''

#With function:-
def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

# How do you prevent a python print() function to print a new line at the end. ANSWER:- end=""
print(a)
print(b)
print(c , end="")
print(d, end="") # type: ignore
'''Output:- a
            b    
            cd'''

# Write a recursive function to calculate the sum of first n natural numbers. 
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n'''

def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n
print(sum(5))

'''Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 '''
def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)

pattern(3)

# Write a python function which converts inches to cms. 
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}cms")


# Strip the word from the list

def rem(l, word):

    for item in l:
        l.remove("am")
        return l

l = ["Sam", "Fam", "Tam", "Wham", "am"]
print(rem(l, "am"))

# Write a python function to remove a given word from a list ad strip it at the same time.

def rems(li, wordd):
    n = []
    for item in li:
        if not(item == wordd):
            n.append(item.strip(wordd))
    return n
li = ["Harry", "Rohan", "Shubham", "an"]
print(rems(li, "an"))

# Write a python function to print multiplication table of a given number. 
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multiply(5)













