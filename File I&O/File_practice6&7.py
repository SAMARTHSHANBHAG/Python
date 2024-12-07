# Write a program to mine a log file and find out whether it contains ‘python’. 
# with open("log.txt", "r") as f:
#     content = f.read()

# if("Python" in content):
#     print("Yes python is present")
# else:
#     print("Python is not present")

# Write a program to find out the line number where python is present from ques 6. 

with open("log.txt", "r") as f:
    lines = f.readlines()

line_number = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present at line {line_number}")
        break
    line_number += 1
else:
    print("python is not present")