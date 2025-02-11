# WHILE LOOPS
i = 1

while(i < 6):
    print(i)
    i += 1


# Write a program to print the content of a list using while loops. 
l1 = ["Apple", "Orange", "Grapes", "Banana"]
i = 0
while(i < len(l1)):
    print(l1[i])
    i+=1


# FOR LOOPS
for i in range(4):
    print(i)


# FOR LOOP WITH ELSE 

l = [3,4,5,6]
for i in l:
    print(i)
else:
    print("Done")

# BREAK KEYWORD
for a in range(20):
    if a == 18:
        break
    
    print(a)

# CONTINUE KEYWORD
for k in range(10):
    if k == 7:
        continue
    print(k)

# PASS KEYWORD
s1= "Samarth"
for i in s1:
    pass    
