'''f = open("file.txt")
print(f.read())
f.close()'''
# Above code is not wrong. But can be optimized with 'with' function

with open("file.txt") as f:
    print(f.read())
# No f.close() required!!
# You dont have to explicitly close the file
