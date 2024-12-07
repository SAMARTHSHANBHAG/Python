# MERGE DICTIONARY AND UPDATE OPERATOR
dict1 = { 'a' :1, 'b': 2 }
dict2 = { 'c' :3, 'd': 4 }

merged = dict1 | dict2
print(merged)

'''# we can now use multiple context managers in a single 'with' statement more cleanly using the parenthesised context manager 

with (
    open('file1.txt') as f1,
    open('file2.txt') as f2,
):
    # Process files
    # '''