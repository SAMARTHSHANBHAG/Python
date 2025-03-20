# Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide user with an option to look it up!
words = {
    "madat": "help",
    "kursi": "Chair",
    "billi": "cat"
}
word = input("Enter the word you want to know the meaning of: ")
print(words[word])

# Write a program to input eight numbers from the user and display all the unique numbers (once).
s = set()
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
print(s)

# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
dict1 = {}

name = input("Enter your name: ")
lang = input("enter the language you know")
dict1.update({name: lang})
name = input("Enter your name: ")
lang = input("enter the language you know")
dict1.update({name: lang})
name = input("Enter your name: ")
lang = input("enter the language you know")
dict1.update({name: lang})
name = input("Enter your name: ")
lang = input("enter the language you know")
dict1.update({name: lang})

print(dict1)

# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# print(s)
# NO, LIST CANNOT BE ADDED IN A SET
