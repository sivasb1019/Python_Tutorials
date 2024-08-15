set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9, 0}
print(set1)
print(set2)

# Set intersection - common values in two sets
print("interaction:", set1 & set2)

set3 = set1 | set2
# Set union - merging 2 sets without duplicate value
print("Union:", set3)

# Set difference
print("Difference set1 - set2:", set1 - set2)
print("Difference set2 - set1:", set2 - set1)

# Set symmatic difference - merging two sets eliminating duplicate values
print("Symmatic difference:", set1 ^ set2)

#To add a data
set1.add(10)
print(set1)
