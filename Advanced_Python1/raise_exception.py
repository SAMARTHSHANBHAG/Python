a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Number cannot be divided by zero !")
else:
    print(f"The division a/b is {a/b}")