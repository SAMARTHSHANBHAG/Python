# Write a program to find the greatest of four numbers entered by the user.
a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("The greatest number is: ", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("The greatest number is: ", a2)

elif(a3>a2 and a3>a1 and a3>a4):
    print("The greatest number is: ", a3)
else:
    print("The greatest number is: ", a4)


# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user

marks1 = int(input("Enter the marks1: "))
marks2 = int(input("Enter the marks2: "))
marks3 = int(input("Enter the marks3: "))

total_percentage = (100*(marks1+ marks2+ marks3))/300

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You pass: ", total_percentage)
else:
    print("You fail: ", total_percentage)

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

phrase1 = "Make a lot of money" 
phrase2 = "buy now"
phrase3 = "subscribe this" 
phrase4 = "click this"

message = input("Enter your message: ")

if((phrase1 in message) or (phrase2 in message) or (phrase3 in message) or (phrase4 in message)):
    print("This message is SPAM")
else:
    print("Comment is not spam")

# Write a program which finds out whether a given name is present in a list or not.
l1 = ["Sam", "Fam", "Tam", "Cham"]
name = input("Enter your name: ")

if(name in l1):
    print("your name is present in the list")
else:
    print("Your name is missing")


# Write a program to find out whether a given post is talking about “Samarth” or not
post = input("Start typing whatever you want: ")

if("Samarth".lower() in post.lower()):
    print("This post is talking about Samarth")
else:
    print("This post is not talking about Samarth")