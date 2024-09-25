import random

a = []

for i in range(3):
    a1 = random.randint(1,7)
    a.append(a1)

print(a)
if a[0] != a[1] and a[1] != a[2] and a[2] != a[0]:
    print(max(a)*100)
if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    if a[1] == a[2] and a[0] == a[1]:
        print(a[1]*1000+10000)
    else:
        print(a[1]*100+1000)
        
