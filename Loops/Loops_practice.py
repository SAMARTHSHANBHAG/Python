#  Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter a number for which you want the multiplication table: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 

l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")

# Attempt problem 1 using while loop.

num1 = int(input("Enter a number for which you want the multiplication table: "))
i = 1

while(i < 11):
    print(f"{num1} X {i} = {num1 * i}")
    i += 1

# Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))
for i in range(2, n):
    if n%i == 0:
        print("Number is not prime")
        break
    else:
        print("Number is a prime number")
        break

# Write a program to find the sum of first n natural numbers using while loop. 
n1 = int(input("Enter a number: "))
i = 1
sum = 0
while(i <= n1):
    sum += i
    i += 1
print(sum)

# Write a program to calculate the factorial of a given number using for loop.
f = int(input("Enter a number: "))
product = 1
for i in range(1, f+1):
    product = product * i

print(product)

'''Write a program to print the following star pattern. 
  * 
 *** 
*****     for n = 3'''
number1 = int(input("Enter a number: "))
for i in range(1, number1+1):
    print(" " * (number1 - i), end="")
    print("*" * (2*i-1), end="")
    print("")

'''Write a program to print the following star pattern: 
* 
** 
***      for n = 3''' 
numb1 = int(input("Enter a number: "))
for i in range(1, numb1+1):
    print("*" * i, end="")
    print("")
'''Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * *              ''' 

numb2 = int(input("Enter a number: "))
for i in range(1, numb2+1):
    if(i==1 or i==numb2):
        print("*" * numb2)
    else:
        print("*", end="")
        print(" " * (numb2-2), end="")
        print("*", end="")
        print("")

# Write a program to print multiplication table of n using for loops in reversed order.
numm = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{numm} X {11-i} = {numm*(11-i)}")
''' Explaination:  1  10
                   2   9
                   3   8
                   4   7
                   5   6
                   6   5
                   7   4
                   8   3
                   9   2
                   10  1   Every pair addition is 11(Our range taken in the code)(11- i will give us the reverse order of 1 to 10)'''
            
