my_set = {1,2,3,4,5}
print("set 1:", my_set)

my_set.add(5)
print("updated set:" , my_set)

set1 = my_set
set2 = {2,4,6,8}
print("set 2:", set2)

print("\nSet 1:" , set1)
print("Set 2:" , set2)
print("difference:" , set1.difference(set2))
print("Symmetrical difference:", set1.symmetric_difference(set2))
print("Union:", set1.union(set2))

