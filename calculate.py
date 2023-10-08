str = input("Enter String: ")
d = l = 0

for i in str:
    if i.isdigit():
       d += 1
    elif i.isalpha(): 
        l += 1
    else:
        pass

print("Letters: ", l)
print("Digits: ", d)