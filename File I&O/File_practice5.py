words = ["Donkey", "Bad", "Ganda"]

with open("4q.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("4q.txt", "w") as f:
    f.write(content) 