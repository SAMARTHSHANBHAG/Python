# Write a program to store 4 fruits in a list entered by the usemarks

fruits = []

f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)

print(fruits)

# Write a program to accept marks of 3 students and display them in a sorted manner.

marks = []

m1 = int(input("Enter your marks: "))
marks.append(m1)
m2 = int(input("Enter your marks: "))
marks.append(m2)
m3 = int(input("Enter your marks: "))
marks.append(m3)

marks.sort()
print(marks)

# Sum of a list
l1 = [2, 4, 6, 8]
print(sum(l1))

# Write a program to count the number of zeros in the following tuple:
t1 = (7, 0, 8, 0, 0, 9)
print(t1.count(0))

