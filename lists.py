l1 = [1, 2, 1, 3, 4, 3, 5, 2]
temp = []
print("Before List: ", l1)

for i in l1:
    if i not in temp:
        temp.append(i)
        l1 = temp
        # print(l1)

print("After List: ", l1)