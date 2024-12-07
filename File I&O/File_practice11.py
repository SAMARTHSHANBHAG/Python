with open("old.txt") as f:
    content = f.read()

with open("Renamed_by_python,txt", "w") as f:
    f.write(content)