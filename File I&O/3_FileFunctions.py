f = open("file.txt")
'''readlines()'''
# lines = f.readlines()
# print(lines, type(lines))

'''readline()'''
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)
# line5 = f.readline()
# print(line5)
# line6 = f.readline()
# print(line6 == "")

'''Readline() using wile loop'''
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()

'''Append something in a file'''
string1 = "Hi samarth you are amazing yaar"

f = open("myfile.txt", "a")

f.write(string1)

f.close