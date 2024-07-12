# this short program shows
# a better way to copy a list

list_1 = [2, 3, 4, 5]
print("list_1:",list_1)

# the easy way to copy a list
list_2 = list_1
print("list_2:",list_2)
# python is awesome

# the hard way to copy a list
# this is how I did it in class
# This is definitely *not* the
# best way to do it
list_3 = []
N = len(list_1)
for i in range(N):
    list_3.append(list_1[i])

print("list_3:",list_3)
