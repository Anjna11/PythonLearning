l1 = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, {"VII" : "S007"}, {"V" : "S009"}, {"VII" : "S005"},]
l2 = []

print(l1)

for _d in l1:
    for val in _d.values():
        l2.append(val)

l = set(l2)
print(l)

# -----------------------------------------------------
d1 = {"V1" : "S001", "V2" : "S002", "V3" : "S001", "V4" : "S005", "V5" : "S007", "V6" : "S009", "V7" : "S005"}

# print(d1)
# print(type(d1))

# print(d1.keys())
# print(d1.values())
# print(d1.get("V"))
# print(d1.items())
unique_set = set()
for val in d1.values():
    unique_set.add(val)

print(unique_set)



    


