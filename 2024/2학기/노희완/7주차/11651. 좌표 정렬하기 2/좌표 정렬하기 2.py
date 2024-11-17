import sys

n = int(sys.stdin.readline().rstrip())

lst = []
for i in range(n):
    [height, weight] = sys.stdin.readline().split()
    lst.append([height, weight])

lst.sort(key = lambda x : (int(x[1]), int(x[0])))

for j in lst:
    print(j[0], j[1])