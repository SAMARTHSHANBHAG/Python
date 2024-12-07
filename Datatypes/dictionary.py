d = {} #EMPTY DICTIONARY
marks = {"Sam": "100",
          "Saw": "44",
          "Sat": "55"
          }
print(marks, type(marks))
print(marks["Sam"])

# Dictionary methods
a = {
    "name": "samarth",
    "from": "India",
    "marks": [100, 99, 88]
}

print(a.items())

print(a.keys())

print(a.values())

a.update({"from": "Canada", "Renuka": "Agra"})
print(a)

print(a.get("name")) #PRINTS "NONE" IF I WRITE "name2" instead of "name"
print(a["name"]) #GIVES AN ERROR IF I WRITE "name2" instead of "name"

value = a.pop("from", "India")
print(value)
print(a)

