name = input("Enter your name: ")

print(f"Good afternoon {name}")

s = "Samarth"
print(s[0:4])
print(s[0:6:2])

#Various string functions
print(len(s))
print(s.endswith("th")) #True
print(s.count("a")) #2
print(s.find("ma")) #2
print(s.replace("ma", "va")) # Savarth
print(s) # Samarth

string1 = "Hello i am good,\tHow are you?\nOkay" #\t:- Gives a tab space , \n :- New line
print(string1)

a = "Samarth is a good \"boy\""
print(a)

num_string = "0123456789"
sliced_num_string = num_string[1:8:2]
print(sliced_num_string)
