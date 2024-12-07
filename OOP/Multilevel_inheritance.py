class human:
    a = 1

class Indian(human):
    b = 2

class Mumbaikar(Indian):
    c = 3

o = human()
print(o.a)
# print(o.b) # Gives error:- AttributeError: 'human' object has no attribute 'b'

o = Indian()
print(o.a, o.b)
# print(o.c) Gives error:- AttributeError: 'Indian' object has no attribute 'c'

o = Mumbaikar()
print(o.a, o.b, o.c)