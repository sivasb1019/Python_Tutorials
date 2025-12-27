set1 = {8, 10, 12, 24, 27, 28, 30}
set2 = {7, 8, 10, 27}
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
set1.add(4)
print(set1)


# Add multiple elements
set2.update([5, 6])
print(set2)

# Remove an element (raises error if not found)
set2.remove(5)
print(set2)

# Remove an element safely (no error if not found)
set2.discard(11)
print(set2)

# Remove and return a random elem99ent
removed = set2.pop()
print(removed)
print(set2)
