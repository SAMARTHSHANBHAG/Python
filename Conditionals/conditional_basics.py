age = int(input("Enter your age: "))
if(age >= 18):
    print("Adult")
else:
    print("Not an adult")



marks = int(input("Enter your marks: "))
if(100 >= marks >= 90):
    print("Excellent")
elif(90 > marks >= 80):
    print("A grade")  
elif(80 > marks >= 70):
    print(" B grade")
elif(70 > marks >= 60):
    print(" C grade")
elif(60 > marks >= 50):
    print(" D grade")
elif(50 > marks >= 0):
    print(" F grade")
else:
    print("Invalid marks")
  