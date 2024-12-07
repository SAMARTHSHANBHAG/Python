class employee:
    language = "py"
    salary = 1200000 # These both are class attributes, since they both are attributes that belong to the class 
    # rather than a particular object.

    @staticmethod 
    def greet():
        print("Good morning")

sam = employee()
sam.name = "Samarth Shanbhag"
sam.greet()
print(sam.language, sam.salary, sam.name) # Here name is Object/ instance attribute and Salary and language are class attributes

rohan = employee()
rohan.name = "Rohan sharma"
print(rohan.salary, rohan.language, rohan.name) # Here name is Object/ instance attribute and Salary and language are class attributes
