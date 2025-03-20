# Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
name = input("Enter your name: ")
print(f"Good afternoon {name}")


letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
# program to replace this code with our actual name and date
print(letter.replace("<|Name|>", "Samarth").replace("<|Date|>", "4th September"))

# Write a program to detect double space in a string.
w = "Samarth is an  amazing boy"
print(w.find("  "))

# Replace the double space from  above problem with single spaces.
print(w.replace("  ", " "))
print(w) # ORIGINAL STRING REMAINS THE SAME AS IT IS IMMUTABLE