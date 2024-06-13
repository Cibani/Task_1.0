# List Operations
print("List Operations:")
list1 = [1, 2, 3]
print("Original List: ", list1)
# Adding an element
list1.append(4)
print("After Adding an element: ", list1)
# Removing an element
list1.remove(2)
print("After Removing an element: ", list1)
# Modifying an element
list1[1] = 5
print("After Modifying an element: ", list1)

# Dictionary Operations
print("\nDictionary Operations:")
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary: ", dict1)
# Adding an element
dict1['d'] = 4
print("After Adding an element: ", dict1)
# Removing an element
del dict1['b']
print("After Removing an element: ", dict1)
# Modifying an element
dict1['a'] = 5
print("After Modifying an element: ", dict1)

# Set Operations
print("\nSet Operations:")
set1 = {1, 2, 3}
print("Original Set: ", set1)
# Adding an element
set1.add(4)
print("After Adding an element: ", set1)
# Removing an element
set1.remove(2)
print("After Removing an element: ", set1)
# Modifying a set (sets are unordered, so we can't modify an individual element like in lists or dictionaries)
set1 = set1.union({5})
print("After Modifying a set: ", set1)
