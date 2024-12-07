class human:
    def __init__(self):
        print("Constructor of human")
    a = 1

class Indian(human):
    def __init__(self):
        print("Constructor of Indian")
    b = 2

class Mumbaikar(Indian):
    def __init__(self):
        super().__init__()
        print("Constructor of Mumbaikar")
    c = 3

# o = human()
# print(o.a)
# print(o.b) # Gives error:- AttributeError: 'human' object has no attribute 'b'

# o = Indian()
# print(o.a, o.b)
# print(o.c) Gives error:- AttributeError: 'Indian' object has no attribute 'c'

o = Mumbaikar()
print(o.a, o.b, o.c)