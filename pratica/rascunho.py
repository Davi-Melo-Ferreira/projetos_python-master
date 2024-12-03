import os


os.system('cls')

a = {1, 8, 2, 4}
b = {3, 5, 4, 6}

# # add
# a.add(3)
# print('add:', a)

# #remove
# a.remove(3)
# print('remove:', a)

# #discard
# a.discard(8)
# print('discard:', a)

# #union
# c = a.union(b)
# print('union:', c)

# #intersection
# c = a.intersection(b)
# print('intersection:', c)
c = a.issuperset(b)
print(c)