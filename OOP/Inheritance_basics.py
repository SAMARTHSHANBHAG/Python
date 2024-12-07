class Employee:
    company = "ITC"
    def show(self):
        print(f"Name of the employee is {self.name} and his salary is {self.salary}")

# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"Name of the employee is {self.name} and his salary is {self.salary}")
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is proficient with {self.language} language")

class Coder(Employee):
    def show(self):
        print(f"Name of the employee is {self.name} and his salary is {self.salary}")



a = Employee()
b = Coder()

print(a.company, b.company)
    