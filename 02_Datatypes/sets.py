s1 = {1, 3, 5, 455, 5, 5, 78}
emptyset = set() # This is required beacuse s = {}, will create an empty dictionary

print(s1, type(s1))
# c = s1[0]
# print(c) TypeError: 'set' object is not subscriptable

s1.add(2)
print(s1)

s1.remove(455)
print(s1)

set1 = {1, 2, 3, 4}
set2 = {77, 99, 88, 12}
print(set1.union(set2))
print(set1.intersection(set2))

print({1}.issubset(s1))