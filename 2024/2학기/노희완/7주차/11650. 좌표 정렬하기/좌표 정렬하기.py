import sys

x = int(sys.stdin.readline().rstrip())

lst = []
for i in range(x):
    [height, weight] = sys.stdin.readline().split()
    lst.append([height, weight])

lst.sort(key = lambda x : (int(x[0]), int(x[1])))

for j in lst:
    print(j[0], j[1])