class worker:
    name = "Harish"
    company = "TCS"
    def show(self):
        print(f"His name is {self.name} and he works for {self.company}")

class Coder:
    language = "Python"
    def printlanguage(self):
        print(f"He is proficient with {self.language} language")

class Programmer(worker, Coder):
    def showLanguage(self):
        print(f" The programmer {self.name} works for is {self.company} and he is an expert in {self.language}")

a = Programmer()
b = Coder
c = worker
a.showLanguage() # Exhibits MULTIPLE INHERITANCE(class programmer inherits both from class worker and class coder )
# b.printlanguage()
# c.show()