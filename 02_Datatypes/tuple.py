a = (1,777, "Samarth") #Tuple with only one element(, is required otherwise python will feel it is an integer datatype)
print(type(a))
print(a.count(1))
s = a.index(777)
print(s)

a[0] = "Samar" # ERROR BECAUSE TUPLE IS IMMUTABLE AND DOES NOT SUPPORT ITEM ASSIGNMENT