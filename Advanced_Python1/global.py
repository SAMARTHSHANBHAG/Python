a = 55

def func():
    global a
    a = 3
    print(a)

func()
print(a)
