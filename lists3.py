l1 = [2, 5, 8, 3, 11, 43, 1, 64, 12]
l2 = [6, 76, 21, 2, 5, 64, 2, 12]
l3 = []

for i in l1:
    if i in l2:
        # print(i)
        l3.append(i)

print(l1)
print(l2)
print(l3)

l4 = [i for i in l1 if i in l2]
print(l4)