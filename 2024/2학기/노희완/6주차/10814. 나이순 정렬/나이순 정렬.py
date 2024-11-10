import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    [age, name] = sys.stdin.readline().split()
    lst.append([age, name])

lst.sort(key = lambda x : int(x[0]))

for i in lst:
    print(i[0], i[1])